from django.urls import path
from . import views

urlpatterns = [
    # Main pages
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('', views.verify_student, name='verify_student'),
    path('generate/', views.generate_certificate, name='generate_certificate'),
    path('page_not_found /', views.page_not_found , name='page_not_found'),
    path('certificates/', views.certificate_list, name='certificate_list'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('stats/', views.stats, name='stats'),
    path('upload/', views.upload_excel, name='upload_excel'),
    path('generate-from-db/', views.generate_certificates_from_db, name='generate_certificates_from_db'),
    path('export-certificates/', views.export_certificates_to_excel, name='export_certificates'),
    path('certificates/export/', views.export_certificates, name='export_certificates'),
    path('certificate_list_view/', views.certificate_list_view, name='certificate_list_view'),
    path('download_excel_template/', views.download_excel_template, name='download_excel_template'),


    path('certificate/<str:certificate_id>/', views.certificate_detail, name='certificate_detail'),
    path('verify/<str:certificate_id>/', views.verify_certificate, name='verify_certificate'),
    
    # Download endpoints
    path('download/<str:certificate_id>/', views.download_certificate, name='download_certificate'),
    path('download-pdf/<str:certificate_id>/', views.download_certificate_pdf, name='download_certificate_pdf'),
    
    # API endpoints
    path('api/verify/<str:certificate_id>/', views.api_verify_certificate, name='api_verify_certificate'),
    
    # Certificate specific pages
#     path('certificate/<uuid:certificate_id>/', views.certificate_detail, name='certificate_detail'),
#     path('verify/<uuid:certificate_id>/', views.verify_certificate, name='verify_certificate'),
    
#     # Download endpoints
#     path('download/<uuid:certificate_id>/', views.download_certificate, name='download_certificate'),
#     path('download-pdf/<uuid:certificate_id>/', views.download_certificate_pdf, name='download_certificate_pdf'),
    
#     # API endpoints
#     path('api/verify/<uuid:certificate_id>/', views.api_verify_certificate, name='api_verify_certificate'),
 ]

