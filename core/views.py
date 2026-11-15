from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.conf import settings
from django.http import JsonResponse
from .models import Category, Package, Vendor, BookingLog

def home_view(request):
    categories = Category.objects.all().order_by('order', 'name')
    packages = Package.objects.filter(is_available=True).select_related('category')
    
    selected_category = request.GET.get('cat', '').strip()
    search_query = request.GET.get('q', '').strip()
    active_category = None

    if selected_category:
        packages = packages.filter(category__slug=selected_category)
        active_category = categories.filter(slug=selected_category).first()

    if search_query:
        packages = packages.filter(
            Q(code__icontains=search_query) |
            Q(title__icontains=search_query) |
            Q(location__icontains=search_query) |
            Q(overview__icontains=search_query) |
            Q(category__name__icontains=search_query)
        )

    admin_phone = getattr(settings, 'ADMIN_WHATSAPP_NUMBER', '94770000000')

    context = {
        'categories': categories,
        'packages': packages,
        'selected_category': selected_category,
        'active_category': active_category,
        'search_query': search_query,
        'admin_phone': admin_phone,
    }
    return render(request, 'index.html', context)


def code_lookup_view(request):
    code_query = request.GET.get('code', '').strip().upper()
    matched_package = None

    if code_query:
        matched_package = Package.objects.filter(code__iexact=code_query).select_related('vendor', 'category').first()

    all_packages = Package.objects.all().select_related('vendor', 'category').order_by('code')

    context = {
        'code_query': code_query,
        'matched_package': matched_package,
        'all_packages': all_packages,
        'admin_phone': getattr(settings, 'ADMIN_WHATSAPP_NUMBER', '94770000000'),
    }
    return render(request, 'code_lookup.html', context)


def search_api_view(request):
    """Live search JSON API — returns matching packages as JSON for instant dropdown."""
    q = request.GET.get('q', '').strip()
    results = []

    if len(q) >= 1:
        packages = Package.objects.filter(
            is_available=True
        ).filter(
            Q(code__icontains=q) |
            Q(title__icontains=q) |
            Q(location__icontains=q) |
            Q(category__name__icontains=q)
        ).select_related('category')[:8]  # Max 8 results in dropdown

        admin_phone = getattr(settings, 'ADMIN_WHATSAPP_NUMBER', '94770000000')

        for p in packages:
            results.append({
                'id': p.id,
                'code': p.code,
                'title': p.title,
                'location': p.location,
                'duration': p.duration,
                'category_name': p.category.name,
                'category_icon': p.category.icon_emoji,
                'category_slug': p.category.slug,
                'image_url': p.image_url,
                'selling_price': str(p.selling_price),
                'original_price': str(p.original_price) if p.original_price else None,
                'badge': p.badge,
                'rating': str(p.rating),
                'whatsapp_url': p.get_whatsapp_booking_url(admin_phone),
                'overview': p.overview[:120] + '...' if len(p.overview) > 120 else p.overview,
            })

    return JsonResponse({'results': results, 'query': q, 'count': len(results)})


import subprocess
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def github_webhook_view(request):
    """
    Auto-updates PythonAnywhere server when GitHub receives a push!
    """
    if request.method == 'POST':
        repo_dir = '/home/NGHL/TravelBook'
        wsgi_file = '/var/www/nghl_pythonanywhere_com_wsgi.py'
        try:
            # 1. Pull latest code from GitHub
            subprocess.run(['git', '-C', repo_dir, 'pull'], check=True, capture_output=True)
            # 2. Touch WSGI file to trigger instant PythonAnywhere auto-reload
            subprocess.run(['touch', wsgi_file], check=True)
            return HttpResponse('PythonAnywhere updated and reloaded successfully!', status=200)
        except Exception as e:
            return HttpResponse(f'Update error: {e}', status=500)
    return HttpResponse('GitHub Webhook endpoint active. Ready for push notifications.')
