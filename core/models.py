from django.db import models
from urllib.parse import quote
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100)
    sinhala_name = models.CharField(max_length=150, blank=True)
    slug = models.SlugField(unique=True)
    icon_emoji = models.CharField(max_length=20, default="🌟", help_text="Emoji or Icon symbol")
    badge = models.CharField(max_length=50, blank=True, help_text="e.g. Popular, Hot, New")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.icon_emoji} {self.name}"


class Vendor(models.Model):
    name = models.CharField(max_length=150, help_text="Vendor or Provider Name")
    business_name = models.CharField(max_length=200, blank=True, help_text="Hotel / Cab / Agency Name")
    service_type = models.CharField(max_length=100, help_text="e.g. Villa Owner, Tour Guide, Cab Service")
    phone = models.CharField(max_length=30)
    whatsapp = models.CharField(max_length=30, help_text="Without '+' (e.g. 94771234567)")
    location = models.CharField(max_length=150, help_text="City / Area (e.g. Ella, Mirissa, Kandy)")
    bank_details = models.TextField(blank=True, help_text="Private bank details for admin transfers")
    private_notes = models.TextField(blank=True, help_text="Private commission agreements, discounts, terms")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.business_name or self.service_type}) - {self.location}"

    @property
    def direct_whatsapp_url(self):
        clean_wa = self.whatsapp.replace("+", "").replace(" ", "").replace("-", "")
        return f"https://wa.me/{clean_wa}"


class Package(models.Model):
    code = models.CharField(max_length=20, unique=True, db_index=True, help_text="Unique Package Code (e.g. TR-01, RM-05, VH-03)")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='packages')
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, blank=True, related_name='packages', help_text="HIDDEN FROM CUSTOMERS! Only Admin can see this.")
    
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=150, help_text="e.g. Ella, Sri Lanka")
    duration = models.CharField(max_length=100, help_text="e.g. 2 Days / 1 Night, Full Day, Per Day")
    
    image_url = models.URLField(max_length=500, help_text="High resolution cover photo URL")
    gallery_urls = models.TextField(blank=True, help_text="Additional photo URLs, one per line")
    
    # Pricing
    selling_price = models.DecimalField(max_digits=12, decimal_places=2, help_text="PUBLIC price shown to customer in LKR")
    original_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True, help_text="Strikethrough price showing discount")
    vendor_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0, help_text="HIDDEN FROM CUSTOMERS! What you pay to the vendor")
    
    # Display details
    badge = models.CharField(max_length=50, blank=True, help_text="e.g. BESTSELLER, INSTANT CONFIRMATION, KLOOK SPECIAL")
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=4.9)
    reviews_count = models.PositiveIntegerField(default=45)
    overview = models.TextField(help_text="Detailed package overview")
    highlights = models.TextField(blank=True, help_text="Bullet points, one per line")
    inclusions = models.TextField(blank=True, help_text="What is included, one per line")
    exclusions = models.TextField(blank=True, help_text="What is not included, one per line")
    
    is_featured = models.BooleanField(default=False, help_text="Pin to top featured section on homepage")
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-is_featured', 'code']

    def __str__(self):
        return f"[{self.code}] {self.title} - Rs. {self.selling_price:,.0f}"

    @property
    def profit_amount(self):
        if self.vendor_cost:
            return self.selling_price - self.vendor_cost
        return self.selling_price

    @property
    def profit_margin_percent(self):
        if self.selling_price and self.vendor_cost:
            return round(((self.selling_price - self.vendor_cost) / self.selling_price) * 100, 1)
        return 100.0

    @property
    def highlights_list(self):
        if self.highlights:
            return [line.strip() for line in self.highlights.splitlines() if line.strip()]
        return []

    @property
    def inclusions_list(self):
        if self.inclusions:
            return [line.strip() for line in self.inclusions.splitlines() if line.strip()]
        return []

    @property
    def exclusions_list(self):
        if self.exclusions:
            return [line.strip() for line in self.exclusions.splitlines() if line.strip()]
        return []

    def get_whatsapp_booking_url(self, admin_phone=None):
        phone = admin_phone or getattr(settings, 'ADMIN_WHATSAPP_NUMBER', '94770000000')
        phone = str(phone).replace("+", "").replace(" ", "").replace("-", "")
        message = (
            f"Hello CeylonGo! 🌴\n\n"
            f"I would like to book the following package:\n"
            f"📌 Package Code: *{self.code}*\n"
            f"🏷️ Title: *{self.title}*\n"
            f"📍 Location: {self.location}\n"
            f"💰 Price: Rs. {self.selling_price:,.0f}\n\n"
            f"Please check availability and confirm details. Thank you!"
        )
        return f"https://wa.me/{phone}?text={quote(message)}"


class BookingLog(models.Model):
    STATUS_CHOICES = [
        ('NEW', 'New Inbound Inquiry'),
        ('VENDOR_CONTACTED', 'Vendor Contacted'),
        ('CONFIRMED', 'Confirmed & Reserved'),
        ('PAID', 'Payment Received'),
        ('COMPLETED', 'Trip Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='bookings')
    customer_name = models.CharField(max_length=150, blank=True)
    customer_phone = models.CharField(max_length=50, blank=True)
    inquiry_date = models.DateField(auto_now_add=True)
    scheduled_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='NEW')
    agreed_selling_price = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    agreed_vendor_cost = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    notes = models.TextField(blank=True, help_text="Notes on customer requirements or vendor confirmations")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking #{self.id} - {self.package.code} ({self.get_status_display()})"
