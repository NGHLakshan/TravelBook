from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Vendor, Package, BookingLog

admin.site.site_header = "CeylonGo Travel & Affiliate Admin"
admin.site.site_title = "CeylonGo Admin Portal"
admin.site.index_title = "Marketplace & Vendor Operations"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'icon_emoji', 'name', 'sinhala_name', 'badge', 'package_count')
    list_display_links = ('id', 'name')
    list_editable = ('order', 'badge')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'sinhala_name')

    def package_count(self, obj):
        return obj.packages.count()
    package_count.short_description = "Packages"


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name', 'business_name', 'service_type', 'phone_display', 'whatsapp_action', 'location', 'package_count', 'is_active')
    list_filter = ('service_type', 'location', 'is_active')
    search_fields = ('name', 'business_name', 'phone', 'whatsapp', 'location', 'private_notes')
    fieldsets = (
        ("Vendor Identity", {
            'fields': ('name', 'business_name', 'service_type', 'is_active')
        }),
        ("Contact Details", {
            'fields': ('phone', 'whatsapp', 'location')
        }),
        ("Confidential Financial & Settlement Details (Private)", {
            'fields': ('bank_details', 'private_notes'),
            'description': "These details are strictly confidential and never visible on the public website."
        }),
    )

    def phone_display(self, obj):
        return format_html('<a href="tel:{}">📞 {}</a>', obj.phone, obj.phone)
    phone_display.short_description = "Phone"

    def whatsapp_action(self, obj):
        return format_html(
            '<a href="{}" target="_blank" style="background:#25D366; color:white; padding:3px 8px; border-radius:4px; text-decoration:none; font-weight:bold;">💬 Chat Vendor</a>',
            obj.direct_whatsapp_url
        )
    whatsapp_action.short_description = "Direct WhatsApp"

    def package_count(self, obj):
        return obj.packages.count()
    package_count.short_description = "Active Services"


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = (
        'code_badge', 
        'title', 
        'category', 
        'vendor_link', 
        'customer_price_display', 
        'vendor_cost_display', 
        'profit_display', 
        'is_featured', 
        'is_available'
    )
    list_filter = ('category', 'is_featured', 'is_available', 'vendor')
    search_fields = ('code', 'title', 'location', 'vendor__name', 'vendor__business_name')
    list_editable = ('is_featured', 'is_available')
    autocomplete_fields = ['vendor']

    fieldsets = (
        ("Package Identification (Public)", {
            'fields': ('code', 'title', 'category', 'badge', 'is_featured', 'is_available')
        }),
        ("Customer Pricing (Public)", {
            'fields': ('selling_price', 'original_price', 'duration', 'location')
        }),
        ("Confidential Vendor & Profit Tracking (Private - Admin Only)", {
            'fields': ('vendor', 'vendor_cost'),
            'description': "Assign which supplier delivers this service and how much they bill you. Your profit is calculated automatically."
        }),
        ("Media & Marketing Content", {
            'fields': ('image_url', 'overview', 'highlights', 'inclusions', 'exclusions')
        }),
        ("Ratings & Reviews", {
            'fields': ('rating', 'reviews_count')
        }),
    )

    def code_badge(self, obj):
        return format_html(
            '<span style="background:#1E293B; color:#F59E0B; font-weight:bold; padding:4px 8px; border-radius:4px; font-family:monospace; font-size:13px;">{}</span>',
            obj.code
        )
    code_badge.short_description = "Code"

    def vendor_link(self, obj):
        if obj.vendor:
            return format_html(
                '<strong>{}</strong><br><small style="color:#64748B;">{} | 📞 {}</small>',
                obj.vendor.name, obj.vendor.business_name, obj.vendor.phone
            )
        return format_html('<span style="color:red;">⚠️ No Vendor Assigned</span>')
    vendor_link.short_description = "Assigned Vendor"

    def customer_price_display(self, obj):
        return format_html('<strong>Rs. {:,.0f}</strong>', obj.selling_price)
    customer_price_display.short_description = "Selling Price"

    def vendor_cost_display(self, obj):
        return format_html('<span style="color:#64748B;">Rs. {:,.0f}</span>', obj.vendor_cost)
    vendor_cost_display.short_description = "Vendor Cost"

    def profit_display(self, obj):
        profit = obj.profit_amount
        percent = obj.profit_margin_percent
        return format_html(
            '<strong style="color:#16A34A;">Rs. {:,.0f}</strong> <span style="font-size:11px; color:#15803D;">({}% margin)</span>',
            profit, percent
        )
    profit_display.short_description = "Your Commission / Profit"


@admin.register(BookingLog)
class BookingLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'package_code', 'customer_name', 'customer_phone', 'status_badge', 'profit_earned', 'created_at')
    list_filter = ('status', 'inquiry_date')
    search_fields = ('package__code', 'customer_name', 'customer_phone', 'notes')

    def package_code(self, obj):
        return obj.package.code
    package_code.short_description = "Package Code"

    def profit_earned(self, obj):
        if obj.agreed_selling_price and obj.agreed_vendor_cost:
            return format_html('<strong style="color:#16A34A;">Rs. {:,.0f}</strong>', (obj.agreed_selling_price - obj.agreed_vendor_cost))
        return "-"
    profit_earned.short_description = "Profit Earned"

    def status_badge(self, obj):
        colors = {
            'NEW': '#3B82F6',
            'VENDOR_CONTACTED': '#F59E0B',
            'CONFIRMED': '#10B981',
            'PAID': '#8B5CF6',
            'COMPLETED': '#059669',
            'CANCELLED': '#EF4444',
        }
        color = colors.get(obj.status, '#6B7280')
        return format_html(
            '<span style="background:{}; color:white; font-size:11px; font-weight:bold; padding:3px 8px; border-radius:12px;">{}</span>',
            color, obj.get_status_display()
        )
    status_badge.short_description = "Status"
