from django.http import HttpResponseRedirect
from django.utils.translation import gettext as _

from custom_models.models import AboutSection, Blog, Brand,Contact, BlogContent, Category, CompanyAddress, Feedback, GlobalInfo, Job, PagesStructer, Product, ProductPDF, ProductPhoto, Project, ProjectPhoto, Service, Slider, Testimonial, global_txt
from django.db.models import Q

from custom_view.RequestProductForm import RequestProductForm
from django.http import JsonResponse





from .forms import ContactForm
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




# دالة لاسترجاع الفئات التي تحتوي فقط على top_category
# def category_list(category=None,catagory_id=None, max_items=None):
#     if category:
#         return Category.objects.filter(
#             (Q(first_has_top_category=category) | Q(second_has_top_category=category)),
#             is_active=True,
#             is_top_category=True  # إضافة شرط التصفية بأن تكون الفئة top_category
#         )
    
#     if catagory_id:


#     return Category.objects.filter(is_active=True, is_top_category=True)  # جلب جميع الفئات النشطة التي هي top_category



def category_list(category=None, catagory_id=None, max_items=None,brand_id=None):



    # إذا لم يتم توفير category أو catagory_id، سنعرض جميع الفئات النشطة التي هي top_category
    categories = Category.objects.filter(is_active=True, is_top_category=True).order_by('-visit_count')




    if category:
        return Category.objects.filter(
            (Q(first_has_top_category=category) | Q(second_has_top_category=category)),
            is_active=True,
            is_top_category=True  # إضافة شرط التصفية بأن تكون الفئة top_category
        ).order_by('-visit_count')
    
    if catagory_id:
        # تصفية الفئة بناءً على الـ id و first_has_top_category
        return Category.objects.filter(
            first_has_top_categoryss=catagory_id,  # نبحث عن الفئة التي لها هذا الـ id
            is_active=True
        ).order_by('-visit_count')






    # if brand_id:
    #     # استرجاع جميع الأقسام المرتبطة بعلامة تجارية معينة
    #     return Category.objects.filter(
    #         Brand__id=brand_id,  # استرجاع الأقسام عبر الربط مع العلامة التجارية
    #         is_active=True
    #     )
    # إذا تم توفير brand_id (الفئات المرتبطة بعلامة تجارية معينة)
    # if brand_id:
    #     return Category.objects.filter(
    #         Q(Brand__id=brand_id) |  # استرجاع الفئات المرتبطة بالعلامة التجارية عبر العلاقات المتعددة
    #         Q(Brand2__id=brand_id) | 
    #         Q(Brand3__id=brand_id) | 
    #         Q(Brand4__id=brand_id) | 
    #         Q(Brand5__id=brand_id),  # تأكد من فحص كل حقل فئة مرتبط بالعلامة التجارية
    #         is_active=True
    #     )

    # إذا تم توفير brand_id (الفئات المرتبطة بعلامة تجارية معينة)
    if brand_id:
        # استخدام علاقة ManyToMany للبحث عن الفئات المرتبطة بالعلامة التجارية
        return Category.objects.filter(
            brandsall__id=brand_id,  # البحث عن الفئات التي ترتبط بالعلامة التجارية عبر علاقة ManyToMany
            is_active=True
        ).order_by('-visit_count')


    










    
    # إذا كان max_items موجودًا، نقوم بتحديد الحد الأقصى لعدد الفئات المسترجعة
    if max_items:
        categories = categories[:max_items]
    
    return categories



def get_sliders(slider_type=None):
    """
    استرجاع السلايدرات بناءً على النوع (صورة أو فيديو).
    إذا لم يتم تحديد نوع، يتم استرجاع جميع السلايدرات النشطة.

    :param slider_type: نوع السلايدر ('image' أو 'video')
    :return: QuerySet يحتوي على السلايدرات المطابقة
    """
    if slider_type:
        return Slider.objects.filter(
            slider_type=slider_type,
            is_active=True
        )
    return Slider.objects.filter(is_active=True)




def get_about_sections(section_type=None, is_active=True):

    filters = {'is_active': is_active}

    if section_type:
        filters['type'] = section_type

    return AboutSection.objects.filter(**filters)








# def get_brand( is_active=True,category=None):

#     filters = {'is_active': is_active}


#     return Brand.objects.filter(**filters)

def get_brand(is_active=True, category=None):
    # استرجاع جميع العلامات التجارية إذا كانت نشطة
    brand = Brand.objects.filter(is_active=is_active).order_by('-visit_count')

    if category:
        # تصفية العلامات التجارية بناءً على الفئات المرتبطة بها
        brand = brand.filter(categoriesAll=category).order_by('-visit_count')  # تصفية العلامات التجارية المرتبطة بالفئة المعينة



    return brand






def get_feedbacks(is_active=True):
    """
    استرجاع التعليقات بناءً على الحالة (نشط أو غير نشط) والنوع.
    :param is_active: الحالة (نشط أو غير نشط).
    :param section_type: النوع (اختياري، يمكنك إضافة حقل النوع في النموذج إذا كان موجودًا).
    :return: QuerySet يحتوي على التعليقات المطابقة.
    """
    filters = {'is_active': is_active}


    return Feedback.objects.filter(**filters)









# دالة لاسترجاع الخدمات النشطة فقط
def service_list(active_only=True):
    """
    Retrieve a list of services based on the given filters.
    :param active_only: Filter only active services if True (default).
    :param max_items: Maximum number of services to retrieve (optional).
    :param keyword: Keyword to search in service title or subtitle (optional).
    :return: QuerySet of filtered services.
    """
    services = Service.objects.all()
    
    # تصفية الخدمات النشطة إذا كان active_only=True
    if active_only:
        services = services.filter(active=True).order_by('-visit_count')

    
    return services













def project_list(active_only=True, include_photos=True, random_order=False):
    """
    Retrieve a list of projects with optional filters and associated photos.
    :param active_only: Filter only active projects if True (default).
    :param include_photos: Include project photos if True (default).
    :return: List of dictionaries containing project, header photo, and associated photos.
    """
    projects = Project.objects.all()

    # تصفية المشاريع النشطة إذا كان active_only=True
    if active_only:
        projects = projects.filter(is_active=True)
    # إضافة الترتيب العشوائي إذا كان random_order=True
    if random_order:
        projects = projects.order_by('?')

    project_data = []
    for project in projects:
        # جلب الصورة الرئيسية (in_header=True)
        header_photo = ProjectPhoto.objects.filter(project=project, in_header=True, is_active=True).first()

        # جلب الصور الأخرى المرتبطة بالمشروع
        photos = ProjectPhoto.objects.filter(project=project, in_header=False, is_active=True) if include_photos else []

        project_data.append({
            "project": project,
            "header_photo": header_photo,
            "photos": photos,
        })

    return project_data







def get_active_testimonials():
    """
    Retrieve active testimonials.
    :return: QuerySet of active testimonials.
    """
    return Testimonial.objects.filter(is_active=True).order_by('-visit_count')










# def product_list(active_only=True, include_photos=True):
#     """
#     Retrieve a list of products with optional filters and associated photos.
#     :param active_only: Filter only active products if True (default).
#     :param include_photos: Include product photos if True (default).
#     :return: List of dictionaries containing product, main photo, and associated photos.
#     """
#     products = Product.objects.all()

#     # تصفية المنتجات النشطة إذا كان active_only=True
#     if active_only:
#         products = products.filter(is_active=True)

#     product_data = []
#     for product in products:
#         # جلب الصورة الرئيسية (is_main=True)
#         main_photo = ProductPhoto.objects.filter(product=product, is_main=True, is_active=True).first()

#         # جلب الصور الأخرى المرتبطة بالمنتج
#         photos = ProductPhoto.objects.filter(product=product, is_main=False, is_active=True) if include_photos else []

#         product_data.append({
#             "product": product,
#             "main_photo": main_photo,
#             "photos": photos,
#         })

#     return product_data


def product_list(active_only=True, include_photos=True, category=None, brand=None, Product_id=None,maxitem=None, order_by=None, random_order=False,in_home=None):
    """
    Retrieve a list of products with optional filters, including category, brand, and associated photos.
    :param active_only: Filter only active products if True (default).
    :param include_photos: Include product photos if True (default).
    :param category: Filter products by category if provided.
    :param brand: Filter products by brand if provided.
    :return: List of dictionaries containing product, main photo, and associated photos.
    """
    # استرجاع المنتجات بناءً على الفلاتر
    products = Product.objects.all()

    # تصفية المنتجات النشطة إذا كان active_only=True
    if active_only:
        products = products.filter(is_active=True).order_by('-visit_count')

    # # تصفية المنتجات حسب الفئة إذا كانت موجودة
    # if category:
    #     products = products.filter(categories=category)
    # تصفية المنتجات حسب الفئة إذا كانت موجودة
    if category:
        # تصفية المنتجات التي تحتوي على الفئة المحددة أو التي تحتوي على الفئة المرتبطة بـ first_has_top_categoryss
        products = products.filter(
            Q(categories=category) | Q(categories__first_has_top_categoryss=category)
        ).order_by('-visit_count')
    # تصفية المنتجات حسب العلامة التجارية إذا كانت موجودة
    if brand:
        products = products.filter(brands=brand).order_by('-visit_count')


    if in_home:
        products = products.filter(in_home=True).order_by('-visit_count')  # استخدم `filter` بعد `all()`
    
        # تصفية المنتجات حسب ID إذا كان موجوداً
    if Product_id:
        products = products.filter(id=Product_id).order_by('-visit_count')


    # إضافة الترتيب العشوائي إذا كان random_order=True
    if random_order:
        products = products.order_by('-visit_count')

    # تحديد الحد الأقصى لعدد المنتجات المعروضة إذا كان maxitem موجوداً
    if maxitem:
        products = products[:maxitem]


    product_data = []
    for product in products:
        # جلب الصورة الرئيسية (is_main=True)
        main_photo = ProductPhoto.objects.filter(product=product, is_main=True, is_active=True).first()

        # جلب الصور الأخرى المرتبطة بالمنتج
        photos = ProductPhoto.objects.filter(product=product, is_active=True) if include_photos else []

        product_data.append({
            "product": product,
            "main_photo": main_photo,
            "photos": photos,
        })

    return product_data






def blog_list(active_only=True, include_content=True,blog_id=None,maxitem=None, order_by=None, random_order=False,in_home=None):
    """
    Retrieve a list of blogs with optional filters and associated content.
    :param active_only: Filter only active blogs if True (default).
    :param include_content: Include blog content if True (default).
    :return: List of dictionaries containing blog, blog content, and associated photos.
    """
    blogs = Blog.objects.all()

    # تصفية المدونات النشطة إذا كان active_only=True
    if active_only:
        blogs = blogs.filter(is_active=True).order_by('-visit_count')


    if in_home:
        blogs = blogs.filter(in_home=True).order_by('-visit_count')  # استخدم `filter` بعد `all()`
    


    # إضافة الترتيب العشوائي إذا كان random_order=True
    if random_order:
        blogs = blogs.order_by('-visit_count')

    # تحديد الحد الأقصى لعدد المنتجات المعروضة إذا كان maxitem موجوداً
    if maxitem:
        blogs = blogs[:maxitem]




    blog_data = []
    for blog in blogs:
        # جلب المحتوى المرتبط بالمدونة
        contents = BlogContent.objects.filter(blog=blog, is_active=True) if include_content else []

        blog_data.append({
            "blog": blog,
            "contents": contents,
        })

    return blog_data

 







def get_CompanyAddress():
    """
    Retrieve active testimonials.
    :return: QuerySet of active testimonials.
    """
    return CompanyAddress.objects.filter(is_active=True)





def get_global_txt():
    """
    Retrieve active testimonials.
    :return: QuerySet of active testimonials.
    """
    return global_txt.objects.filter()


def get_GlobalInfo():
    """
    Retrieve active testimonials.
    :return: QuerySet of active testimonials.
    """
    return GlobalInfo.objects.filter(is_active=True)




# دالة لاسترجاع الخدمات النشطة فقط
def Job_list(active_only=True, job_id=None,in_home=None):
    jobs = Job.objects.all()
    
    # تصفية الخدمات النشطة إذا كان active_only=True
    if active_only:
        jobs = jobs.filter(is_active=True)  # استخدم `filter` بعد `all()`
    if in_home:
        jobs = jobs.filter(in_home=True)  # استخدم `filter` بعد `all()`
    
    # تصفية الوظيفة بناءً على `job_id` إذا تم توفيره
    if job_id:
        jobs = jobs.filter(id=job_id)  # تصفية الوظائف بناءً على الـ id
    
    return jobs















# def get_product_pdfs(product_id=None):

#     pdfs = ProductPDF.objects.all()

#     if product_id:
#         pdfs = pdfs.filter(product__id=product_id)  # تصفية بناءً على المنتج
    
#     return pdfs

def get_product_pdfs(product_id=None):
    """ جلب ملفات PDF المرتبطة بمنتج معين """
    if product_id:
        return ProductPDF.objects.filter(product__id=product_id)
    return ProductPDF.objects.all()











def home(request):
    message = _("Welcome to our website!")
    
    # معالجة بيانات نموذج الاتصال إذا تم إرسالها
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # حفظ بيانات النموذج في قاعدة البيانات
            messages.success(request, _("Your message has been sent successfully!"))
            return redirect('custom_view:contact')  # إعادة توجيه المستخدم إلى نفس الصفحة بعد الإرسال
    else:
        form = ContactForm()

    # استرجاع باقي البيانات لعرض الصفحة
    page_structures = PagesStructer.objects.filter(pages__title='home',is_active=True).order_by('order')
    top_category = category_list()  # استدعاء دالة الفئات
    video_sliders = get_sliders(slider_type='video')
    about_sections_ = get_about_sections(is_active=True, section_type='photo')
    active_feedbacks = get_feedbacks(is_active=True)
    active_services = service_list()
    active_projects_with_photos = project_list(random_order=True)
    testimonials = get_active_testimonials()
    product_list_section = product_list(maxitem=50,random_order=True,in_home=True)
    blog_list_section = blog_list(maxitem=50,random_order=True,in_home=True)
    get_CompanyAddress_section = get_CompanyAddress()
    get_GlobalInfo_section = get_GlobalInfo()

    Job_list_section = Job_list()

    get_global_txt_section = get_global_txt()


 



    return render(request, 'templet_app/index.html', {
        'structures': page_structures,
        'message': message,
        'categories': top_category,
        'video_sliders': video_sliders,
        'about_sections_': about_sections_,
        'active_feedbacks': active_feedbacks,
        'active_services': active_services,
        'active_projects': active_projects_with_photos,
        'testimonials': testimonials,
        'product_list_section': product_list_section,
        'blog_list_section': blog_list_section,
        'get_CompanyAddress_section': get_CompanyAddress_section,
        'get_GlobalInfo_section': get_GlobalInfo_section,
        'contact_form': form,  # إضافة النموذج إلى القالب

        'Job_list_section': Job_list_section,  
        'get_global_txt_section': get_global_txt_section,  





    })






# def contact(request):

#     # استدعاء دالة category_list لعرض الفئات
#     top_category = category_list()  # استدعاء الدالة للحصول على الفئات التي هي top_category فقط
#     video_sliders = get_sliders(slider_type='video')


#     return render(request, 'templet_app/contact.html', {'categories': top_category,
#         'video_sliders': video_sliders,})


def contact(request):
    message = _("Welcome to our website!")
    
    # معالجة بيانات نموذج الاتصال إذا تم إرسالها
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # حفظ بيانات النموذج في قاعدة البيانات
            messages.success(request, _("Your message has been sent successfully!"))
            return redirect('custom_view:contact')  # إعادة توجيه المستخدم إلى نفس الصفحة بعد الإرسال
    else:
        form = ContactForm()

    # استرجاع باقي البيانات لعرض الصفحة
    page_structures = PagesStructer.objects.filter(pages__title='contact',is_active=True).order_by('order')
    top_category = category_list()  # استدعاء دالة الفئات
    video_sliders = get_sliders(slider_type='video')
    about_sections_ = get_about_sections(is_active=True, section_type='photo')
    active_feedbacks = get_feedbacks(is_active=True)
    active_services = service_list()
    active_projects_with_photos = project_list()
    testimonials = get_active_testimonials()
    product_list_section = product_list()
    blog_list_section = blog_list()
    get_CompanyAddress_section = get_CompanyAddress()
    get_GlobalInfo_section = get_GlobalInfo()

    get_global_txt_section = get_global_txt()



 



    return render(request, 'templet_app/contact.html', {
        'structures': page_structures,
        'message': message,
        'categories': top_category,
        'video_sliders': video_sliders,
        'about_sections_': about_sections_,
        'active_feedbacks': active_feedbacks,
        'active_services': active_services,
        'active_projects': active_projects_with_photos,
        'testimonials': testimonials,
        'product_list': product_list_section,
        'blog_list_section': blog_list_section,
        'get_CompanyAddress_section': get_CompanyAddress_section,
        'get_GlobalInfo_section': get_GlobalInfo_section,
        'contact_form': form,  # إضافة النموذج إلى القالب

        'get_global_txt_section': get_global_txt_section,  





    })







 

# فقط شيل ال blog list  من
def blog_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)

    blog_list_section = blog_list()


    top_category = category_list()  # استدعاء دالة الفئات
    video_sliders = get_sliders(slider_type='video')
    about_sections_ = get_about_sections(is_active=True, section_type='photo')
    active_feedbacks = get_feedbacks(is_active=True)
    active_services = service_list()
    active_projects_with_photos = project_list()
    testimonials = get_active_testimonials()
    product_list_section = product_list()
    get_CompanyAddress_section = get_CompanyAddress()
    get_GlobalInfo_section = get_GlobalInfo()

    get_global_txt_section = get_global_txt()

    page_structures = PagesStructer.objects.filter(pages__title='blog_detail',is_active=True).order_by('order')


    return render(request, 'templet_app/blog_sigle.html', {

                'structures': page_structures,

        'blog': blog,
        'blog_list_section': blog_list_section,



        'categories': top_category,
        'video_sliders': video_sliders,
        'about_sections_': about_sections_,
        'active_feedbacks': active_feedbacks,
        'active_services': active_services,
        'active_projects': active_projects_with_photos,
        'testimonials': testimonials,
        'product_list': product_list_section,
        'get_CompanyAddress_section': get_CompanyAddress_section,
        'get_GlobalInfo_section': get_GlobalInfo_section,
                'get_global_txt_section': get_global_txt_section,  

        })



















def blog_archive(request):
    message = _("Welcome to our website!")
    
    # معالجة بيانات نموذج الاتصال إذا تم إرسالها
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # حفظ بيانات النموذج في قاعدة البيانات
            messages.success(request, _("Your message has been sent successfully!"))
            return redirect('custom_view:contact')  # إعادة توجيه المستخدم إلى نفس الصفحة بعد الإرسال
    else:
        form = ContactForm()

    # استرجاع باقي البيانات لعرض الصفحة
    page_structures = PagesStructer.objects.filter(pages__title='blog_archive',is_active=True).order_by('order')
    top_category = category_list()  # استدعاء دالة الفئات
    video_sliders = get_sliders(slider_type='video')
    about_sections_ = get_about_sections(is_active=True, section_type='photo')
    active_feedbacks = get_feedbacks(is_active=True)
    active_services = service_list()
    active_projects_with_photos = project_list()
    testimonials = get_active_testimonials()
    product_list_section = product_list()
    blog_list_section = blog_list()
    get_CompanyAddress_section = get_CompanyAddress()
    get_GlobalInfo_section = get_GlobalInfo()


    get_global_txt_section = get_global_txt()


 



    return render(request, 'templet_app/blog_archive.html', {
        'structures': page_structures,
        'message': message,
        'categories': top_category,
        'video_sliders': video_sliders,
        'about_sections_': about_sections_,
        'active_feedbacks': active_feedbacks,
        'active_services': active_services,
        'active_projects': active_projects_with_photos,
        'testimonials': testimonials,
        'product_list': product_list_section,
        'blog_list_section': blog_list_section,
        'get_CompanyAddress_section': get_CompanyAddress_section,
        'get_GlobalInfo_section': get_GlobalInfo_section,
        'contact_form': form,  # إضافة النموذج إلى القالب


                'get_global_txt_section': get_global_txt_section,  




    })

















# فقط شيل ال blog list  من
def project_single(request, project_id):
    try:
        # جلب بيانات المشروع بناءً على ID
        project = Project.objects.get(id=project_id)

        # جلب الصورة الرئيسية للمشروع
        header_photo = ProjectPhoto.objects.filter(project=project, in_header=True, is_active=True).first()

        # جلب الصور الأخرى المرتبطة بالمشروع
        photos = ProjectPhoto.objects.filter(project=project, in_header=False, is_active=True)

        # استدعاء باقي الدوال
        blog_list_section = blog_list()
        top_category = category_list()  # استدعاء دالة الفئات
        video_sliders = get_sliders(slider_type='video')
        about_sections_ = get_about_sections(is_active=True, section_type='photo')
        active_feedbacks = get_feedbacks(is_active=True)
        active_services = service_list()
        testimonials = get_active_testimonials()
        product_list_section = product_list()
        get_CompanyAddress_section = get_CompanyAddress()
        get_GlobalInfo_section = get_GlobalInfo()
        get_global_txt_section = get_global_txt()

        # جلب الهياكل الخاصة بالصفحة
        page_structures = PagesStructer.objects.filter(pages__title='project_single',is_active=True).order_by('order')

        # تمرير البيانات إلى القالب
        return render(request, 'templet_app/project_single.html', {
            'structures': page_structures,
            'project': project,
            'header_photo': header_photo,
            'photos': photos,
            'blog_list_section': blog_list_section,
            'categories': top_category,
            'video_sliders': video_sliders,
            'about_sections_': about_sections_,
            'active_feedbacks': active_feedbacks,
            'active_services': active_services,
            'testimonials': testimonials,
            'product_list': product_list_section,
            'get_CompanyAddress_section': get_CompanyAddress_section,
            'get_GlobalInfo_section': get_GlobalInfo_section,

                'get_global_txt_section': get_global_txt_section,  



        })

    except Project.DoesNotExist:
        # إذا لم يتم العثور على المشروع، يمكن عرض صفحة خطأ أو إعادة توجيه
        return render(request, 'templet_app/404.html', status=404)











 

# فقط شيل ال blog list  من
def catagory_detail(request, category_id):
    category = Category.objects.get(id=category_id)

    blog_list_section = blog_list()


    sub_category = category_list(catagory_id=category_id)  # استدعاء دالة الفئات
    top_category = category_list()  # استدعاء دالة الفئات

    video_sliders = get_sliders(slider_type='video')
    about_sections_ = get_about_sections(is_active=True, section_type='photo')
    active_feedbacks = get_feedbacks(is_active=True)
    active_services = service_list()
    active_projects_with_photos = project_list()
    testimonials = get_active_testimonials()
    product_list_section = product_list(category=category_id)
    get_CompanyAddress_section = get_CompanyAddress()
    get_GlobalInfo_section = get_GlobalInfo()
    category_brand = get_brand(category=category_id)

    page_structures = PagesStructer.objects.filter(pages__title='catagory_detail',is_active=True).order_by('order')


    get_global_txt_section = get_global_txt()



    # إعداد Pagination
    paginator = Paginator(product_list_section, 15)  # عرض 10 منتجات لكل صفحة
    page = request.GET.get('page')  # الحصول على رقم الصفحة من الطلب
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)  # إذا كانت الصفحة غير صالحة، يتم عرض الصفحة الأولى
    except EmptyPage:
        products = paginator.page(paginator.num_pages)  # إذا كانت الصفحة خارج النطاق، يتم عرض الصفحة الأخيرة













    return render(request, 'templet_app/catagory_detail.html', {

                'structures': page_structures,

        'blog_list_section': blog_list_section,

        'category_brand': category_brand,

        'category': category,
        'sub_category': sub_category,

        'categories': top_category,
        'video_sliders': video_sliders,
        'about_sections_': about_sections_,
        'active_feedbacks': active_feedbacks,
        'active_services': active_services,
        'active_projects': active_projects_with_photos,
        'testimonials': testimonials,
        'product_list': products,
        'get_CompanyAddress_section': get_CompanyAddress_section,
        'get_GlobalInfo_section': get_GlobalInfo_section,
                        'get_global_txt_section': get_global_txt_section,  

        })





 

# فقط شيل ال blog list  من
def brand_detail(request, brand_id):

    brand = Brand.objects.get(id=brand_id)

    blog_list_section = blog_list()


    sub_category = category_list(brand_id=brand_id)  # استدعاء دالة الفئات
    top_category = category_list()  # استدعاء دالة الفئات

    video_sliders = get_sliders(slider_type='video')
    about_sections_ = get_about_sections(is_active=True, section_type='photo')
    active_feedbacks = get_feedbacks(is_active=True)
    active_services = service_list()
    active_projects_with_photos = project_list()
    testimonials = get_active_testimonials()
    product_list_section = product_list(brand=brand_id)
    get_CompanyAddress_section = get_CompanyAddress()
    get_GlobalInfo_section = get_GlobalInfo()
    category_brand = get_brand()

    page_structures = PagesStructer.objects.filter(pages__title='brand_detail',is_active=True).order_by('order')



    get_global_txt_section = get_global_txt()





    # إعداد Pagination
    paginator = Paginator(product_list_section, 15)  # عرض 10 منتجات لكل صفحة
    page = request.GET.get('page')  # الحصول على رقم الصفحة من الطلب
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)  # إذا كانت الصفحة غير صالحة، يتم عرض الصفحة الأولى
    except EmptyPage:
        products = paginator.page(paginator.num_pages)  # إذا كانت الصفحة خارج النطاق، يتم عرض الصفحة الأخيرة











    return render(request, 'templet_app/brand_detail.html', {

                'structures': page_structures,
        'brand': brand,

        'blog_list_section': blog_list_section,

        'category_brand': category_brand,

        'sub_category': sub_category,

        'categories': top_category,
        'video_sliders': video_sliders,
        'about_sections_': about_sections_,
        'active_feedbacks': active_feedbacks,
        'active_services': active_services,
        'active_projects': active_projects_with_photos,
        'testimonials': testimonials,
        'product_list': products,
        'get_CompanyAddress_section': get_CompanyAddress_section,
        'get_GlobalInfo_section': get_GlobalInfo_section,
                                'get_global_txt_section': get_global_txt_section,  

        })















# فقط شيل ال blog list  من
def Service_detail(request, service_id):
    service = Service.objects.get(id=service_id)

    blog_list_section = blog_list()


    sub_category = category_list()  # استدعاء دالة الفئات
    top_category = category_list()  # استدعاء دالة الفئات

    video_sliders = get_sliders(slider_type='video')
    about_sections_ = get_about_sections(is_active=True, section_type='photo')
    active_feedbacks = get_feedbacks(is_active=True)
    active_services = service_list()
    active_projects_with_photos = project_list()
    testimonials = get_active_testimonials()
    product_list_section = product_list()
    get_CompanyAddress_section = get_CompanyAddress()
    get_GlobalInfo_section = get_GlobalInfo()
    category_brand = get_brand()

    page_structures = PagesStructer.objects.filter(pages__title='service_single',is_active=True).order_by('order')



    get_global_txt_section = get_global_txt()











    return render(request, 'templet_app/service_single.html', {

                'structures': page_structures,

        'blog_list_section': blog_list_section,

        'category_brand': category_brand,

        'service': service,
        'sub_category': sub_category,

        'categories': top_category,
        'video_sliders': video_sliders,
        'about_sections_': about_sections_,
        'active_feedbacks': active_feedbacks,
        'active_services': active_services,
        'active_projects': active_projects_with_photos,
        'testimonials': testimonials,
        'product_list': product_list_section,
        'get_CompanyAddress_section': get_CompanyAddress_section,
        'get_GlobalInfo_section': get_GlobalInfo_section,
                                        'get_global_txt_section': get_global_txt_section,  

        })



















def Product_detail(request, Product_id):
    # product = Product.objects.get(id=Product_id)
    product = product_list(Product_id=Product_id)



    # pdfs = get_product_pdfs(product_id=Product_id)

    # جلب ملفات PDF المرتبطة بالمنتج
    # pdfs = ProductPDF.objects.filter(product=Product_id)
    # جلب ملفات PDF المرتبطة بالمنتج
    pdfs = get_product_pdfs(product_id=Product_id)




    # إذا تم إرسال النموذج
    if request.method == 'POST':
        form = RequestProductForm(request.POST)
        if form.is_valid():
            form.save()  # حفظ النموذج في قاعدة البيانات
            # يمكنك إضافة رد أو إعادة توجيه هنا بعد حفظ النموذج
            return HttpResponseRedirect(request.path)  # إعادة التوجيه إلى نفس الصفحة
    else:
        form = RequestProductForm()  # استرجاع نموذج فارغ في حالة GET












    blog_list_section = blog_list()


    sub_category = category_list()  # استدعاء دالة الفئات
    top_category = category_list()  # استدعاء دالة الفئات

    video_sliders = get_sliders(slider_type='video')
    about_sections_ = get_about_sections(is_active=True, section_type='photo')
    active_feedbacks = get_feedbacks(is_active=True)
    active_services = service_list()
    active_projects_with_photos = project_list()
    testimonials = get_active_testimonials()
    product_list_section = product_list()
    get_CompanyAddress_section = get_CompanyAddress()
    get_GlobalInfo_section = get_GlobalInfo()
    category_brand = get_brand()

    page_structures = PagesStructer.objects.filter(pages__title='product_single',is_active=True).order_by('order')


    get_global_txt_section = get_global_txt()

 










    return render(request, 'templet_app/product_single.html', {

                'structures': page_structures,
        'product': product,

        'blog_list_section': blog_list_section,

        'category_brand': category_brand,

        'sub_category': sub_category,

        'categories': top_category,
        'video_sliders': video_sliders,
        'about_sections_': about_sections_,
        'active_feedbacks': active_feedbacks,
        'active_services': active_services,
        'active_projects': active_projects_with_photos,
        'testimonials': testimonials,
        'product_list': product_list_section,
        'get_CompanyAddress_section': get_CompanyAddress_section,
        'get_GlobalInfo_section': get_GlobalInfo_section,
        'pdfs': pdfs,  # تمرير ملفات PDF إلى القالب


        'form': form,  # إضافة النموذج إلى السياق

                                        'get_global_txt_section': get_global_txt_section,  


        })






















def about_us(request):
    message = _("Welcome to our website!")
    
    # معالجة بيانات نموذج الاتصال إذا تم إرسالها
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # حفظ بيانات النموذج في قاعدة البيانات
            messages.success(request, _("Your message has been sent successfully!"))
            return redirect('custom_view:contact')  # إعادة توجيه المستخدم إلى نفس الصفحة بعد الإرسال
    else:
        form = ContactForm()

    # استرجاع باقي البيانات لعرض الصفحة
    page_structures = PagesStructer.objects.filter(pages__title='about_us',is_active=True).order_by('order')
    top_category = category_list()  # استدعاء دالة الفئات
    video_sliders = get_sliders(slider_type='video')
    about_sections_ = get_about_sections(is_active=True, section_type='photo')
    active_feedbacks = get_feedbacks(is_active=True)
    active_services = service_list()
    active_projects_with_photos = project_list()
    testimonials = get_active_testimonials()
    product_list_section = product_list()
    blog_list_section = blog_list()
    get_CompanyAddress_section = get_CompanyAddress()
    get_GlobalInfo_section = get_GlobalInfo()




    get_global_txt_section = get_global_txt()




    return render(request, 'templet_app/about_us.html', {
        'structures': page_structures,
        'message': message,
        'categories': top_category,
        'video_sliders': video_sliders,
        'about_sections_': about_sections_,
        'active_feedbacks': active_feedbacks,
        'active_services': active_services,
        'active_projects': active_projects_with_photos,
        'testimonials': testimonials,
        'product_list': product_list_section,
        'blog_list_section': blog_list_section,
        'get_CompanyAddress_section': get_CompanyAddress_section,
        'get_GlobalInfo_section': get_GlobalInfo_section,
        'contact_form': form,  # إضافة النموذج إلى القالب


                                        'get_global_txt_section': get_global_txt_section,  




    })
















def career_page(request):
    message = _("Welcome to our website!")
    
    # معالجة بيانات نموذج الاتصال إذا تم إرسالها
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # حفظ بيانات النموذج في قاعدة البيانات
            messages.success(request, _("Your message has been sent successfully!"))
            return redirect('custom_view:contact')  # إعادة توجيه المستخدم إلى نفس الصفحة بعد الإرسال
    else:
        form = ContactForm()

    # استرجاع باقي البيانات لعرض الصفحة
    page_structures = PagesStructer.objects.filter(pages__title='career_page',is_active=True).order_by('order')
    top_category = category_list()  # استدعاء دالة الفئات
    video_sliders = get_sliders(slider_type='video')
    about_sections_ = get_about_sections(is_active=True, section_type='photo')
    active_feedbacks = get_feedbacks(is_active=True)
    active_services = service_list()
    active_projects_with_photos = project_list()
    testimonials = get_active_testimonials()
    product_list_section = product_list()
    blog_list_section = blog_list()
    get_CompanyAddress_section = get_CompanyAddress()
    get_GlobalInfo_section = get_GlobalInfo()

    Job_list_section = Job_list()



    get_global_txt_section = get_global_txt()




    return render(request, 'templet_app/career_page.html', {
        'structures': page_structures,
        'message': message,
        'categories': top_category,
        'video_sliders': video_sliders,
        'about_sections_': about_sections_,
        'active_feedbacks': active_feedbacks,
        'active_services': active_services,
        'active_projects': active_projects_with_photos,
        'testimonials': testimonials,
        'product_list': product_list_section,
        'blog_list_section': blog_list_section,
        'get_CompanyAddress_section': get_CompanyAddress_section,
        'get_GlobalInfo_section': get_GlobalInfo_section,
        'contact_form': form,  # إضافة النموذج إلى القالب

        'Job_list_section': Job_list_section,  
                                        'get_global_txt_section': get_global_txt_section,  





    })










def job_detail(request, job_id):
    # product = Product.objects.get(id=Product_id)




    Job_list_section = Job_list(job_id=job_id)




    # إذا تم إرسال النموذج
    if request.method == 'POST':
        form = RequestProductForm(request.POST)
        if form.is_valid():
            form.save()  # حفظ النموذج في قاعدة البيانات
            # يمكنك إضافة رد أو إعادة توجيه هنا بعد حفظ النموذج
            return HttpResponseRedirect(request.path)  # إعادة التوجيه إلى نفس الصفحة
    else:
        form = RequestProductForm()  # استرجاع نموذج فارغ في حالة GET












    blog_list_section = blog_list()


    sub_category = category_list()  # استدعاء دالة الفئات
    top_category = category_list()  # استدعاء دالة الفئات

    video_sliders = get_sliders(slider_type='video')
    about_sections_ = get_about_sections(is_active=True, section_type='photo')
    active_feedbacks = get_feedbacks(is_active=True)
    active_services = service_list()
    active_projects_with_photos = project_list()
    testimonials = get_active_testimonials()
    product_list_section = product_list()
    get_CompanyAddress_section = get_CompanyAddress()
    get_GlobalInfo_section = get_GlobalInfo()
    category_brand = get_brand()

    page_structures = PagesStructer.objects.filter(pages__title='job_detail',is_active=True).order_by('order')



 

    get_global_txt_section = get_global_txt()









    return render(request, 'templet_app/job_detail.html', {

                'structures': page_structures,

        'blog_list_section': blog_list_section,

        'category_brand': category_brand,

        'sub_category': sub_category,

        'categories': top_category,
        'video_sliders': video_sliders,
        'about_sections_': about_sections_,
        'active_feedbacks': active_feedbacks,
        'active_services': active_services,
        'active_projects': active_projects_with_photos,
        'testimonials': testimonials,
        'product_list': product_list_section,
        'get_CompanyAddress_section': get_CompanyAddress_section,
        'get_GlobalInfo_section': get_GlobalInfo_section,
        

        'form': form,  # إضافة النموذج إلى السياق

        'Job_list_section': Job_list_section,  

                                        'get_global_txt_section': get_global_txt_section,  

        })




def submit_contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            return JsonResponse({'success': True, 'message': 'تم إرسال الطلب بنجاح!'})
        else:
            return JsonResponse({'success': False, 'message': 'خطأ في البيانات المُدخلة!'}, status=400)
    return JsonResponse({'success': False, 'message': 'طلب غير صالح!'}, status=400)