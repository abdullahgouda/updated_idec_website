from django.db import models

# جدول السلايدر
class Slider(models.Model):
    SLIDER_TYPE_CHOICES = [
        ('image', 'صورة'),
        ('video', 'فيديو'),
    ]

    slider_type = models.CharField(
        max_length=255,
        choices=SLIDER_TYPE_CHOICES,
        default='image', null=True, blank=True
    )
    title = models.CharField(max_length=255, null=True, blank=True)
    sub_title = models.CharField(max_length=255, null=True, blank=True)

    # الحقول الجديدة
    image = models.ImageField(upload_to='sliders/', null=True, blank=True)  # لإضافة صورة
    video = models.FileField(upload_to='sliders/videos/', null=True, blank=True)  # لإضافة فيديو

    visit_count = models.IntegerField(default=0, null=True, blank=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title if self.title else "Slider (No Title)"


# جدول الخدمة
class Service(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    overview = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='services/', null=True, blank=True)
    active = models.BooleanField(default=True)  # الحقل الجديد
    html_content = models.TextField(blank=True, null=True)
    visit_count = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.title

# جدول الاتصال
class Contact(models.Model):
    STATUS_CHOICES = [
        ('new', 'جديد'),
        ('in_progress', 'تحت المعالجة'),
        ('resolved', 'تم الحل'),
        ('closed', 'مغلق'),
    ]


    file_types = models.ForeignKey(
        "FileType", 
        on_delete=models.SET_NULL,  # إذا تم حذف النوع، لا نحذف ملفات PDF
        null=True, 
        blank=True,
        related_name='pdfss'
    )

    product = models.ForeignKey("Product", on_delete=models.CASCADE, null=True, blank=True)


    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()
    is_active = models.BooleanField(default=True)

    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='new'
    )  # حقل الحالة الجديد

    def __str__(self):
        return f"{self.name} - {self.get_status_display()}"

# جدول البانر
class Banner(models.Model):
    title = models.CharField(max_length=255)
    title_ar = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField(upload_to='banners/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

# جدول التعليقات
class Feedback(models.Model):
    title = models.CharField(max_length=255)
    icon = models.CharField(max_length=255, null=True, blank=True)
    number = models.PositiveIntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

# جدول الشهادات
class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    quote = models.TextField()
    is_active = models.BooleanField(default=True)
    visit_count = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name

# جدول الفئات
class Category(models.Model):
    name = models.CharField(max_length=255)
    # name_ar = models.CharField(max_length=255, null=True, blank=True)
    sub_title = models.CharField(max_length=255, null=True, blank=True)
    # sub_title_ar = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    # description_ar = models.TextField(null=True, blank=True)
    is_top_category = models.BooleanField(default=False)
    first_has_top_categoryss = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="first_has_top_category")
    image = models.ImageField(upload_to='categories/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    # created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    # updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    visit_count = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.name

# جدول العلامات التجارية
class Brand(models.Model):
    name = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    logo = models.ImageField(upload_to='brands/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    visit_count = models.IntegerField(default=0, null=True, blank=True)

    # ربط المنتج مع الأقسام
    categories = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,  # يمكنك تحديد أي سياسة حذف تناسبك
        related_name='Brand',
        blank=True,
        null=True  # إذا كنت تريد أن يكون الحقل اختياريًا
    )

    categories2 = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,  # يمكنك تحديد أي سياسة حذف تناسبك
        related_name='Brand2',
        blank=True,
        null=True  # إذا كنت تريد أن يكون الحقل اختياريًا
    )


    categories3 = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,  # يمكنك تحديد أي سياسة حذف تناسبك
        related_name='Brand3',
        blank=True,
        null=True  # إذا كنت تريد أن يكون الحقل اختياريًا
    )

    categories4 = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,  # يمكنك تحديد أي سياسة حذف تناسبك
        related_name='Brand4',
        blank=True,
        null=True  # إذا كنت تريد أن يكون الحقل اختياريًا
    )

    categories5 = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,  # يمكنك تحديد أي سياسة حذف تناسبك
        related_name='Brand5',
        blank=True,
        null=True  # إذا كنت تريد أن يكون الحقل اختياريًا
    )

    # ربط العلامة التجارية بالفئات باستخدام علاقة many-to-many
    categoriesAll = models.ManyToManyField(
        Category, 
        related_name='brandsall', 
        blank=True  # يمكن أن يكون الحقل اختياريًا
    )


    def __str__(self):
        return self.name

# جدول المدونة
class Blog(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    html_content = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='Blog/', null=True, blank=True)
    in_home = models.BooleanField(default=False)
    visit_count = models.IntegerField(default=0, null=True, blank=True)

    # ربط المنتج مع الأقسام
    categories = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,  # يمكنك تحديد أي سياسة حذف تناسبك
        related_name='Blog',
        blank=True,
        null=True  # إذا كنت تريد أن يكون الحقل اختياريًا
    )
    def __str__(self):
        return self.title

# جدول محتوى المدونة
class BlogContent(models.Model):

    blog = models.ForeignKey(
        Blog, 
        on_delete=models.CASCADE, 
        related_name='contents'
    )  # ربط المحتوى بالمدونة
    header = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='blog_content/', null=True, blank=True)
    ordering = models.IntegerField( null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.header



# جدول المشاريع
class Project(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255, null=True, blank=True)
    year = models.IntegerField()
    project_type = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    html_content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

# جدول صور المشروع
class ProjectPhoto(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='project_photos/')
    in_header = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Photo for {self.project.title}"

# جدول عن القسم
class AboutSection(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='about_section/', null=True, blank=True)
    if_about_page = models.BooleanField(default=True)
    video = models.URLField(null=True, blank=True)
    type = models.CharField(max_length=50, choices=[('video', 'Video'), ('photo', 'Photo')])
    is_active = models.BooleanField(default=True)
    # حقل TextField لتخزين HTML
    html_content = models.TextField(blank=True, null=True)
    # free_section = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

# جدول محتوى القسم
class AboutSectionContent(models.Model):
    title = models.CharField(max_length=255)
    title_ar = models.CharField(max_length=255, null=True, blank=True)
    sub_title = models.CharField(max_length=255, null=True, blank=True)
    sub_title_ar = models.CharField(max_length=255, null=True, blank=True)
    about_section = models.ForeignKey(AboutSection, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

# جدول المنتج
class Product(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    in_home = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    visit_count = models.IntegerField(default=0, null=True, blank=True)

    # ربط المنتج مع الأقسام
    categories = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE,  # يمكنك تحديد أي سياسة حذف تناسبك
        related_name='products',
        blank=True,
        null=True  # إذا كنت تريد أن يكون الحقل اختياريًا
    )
    
    # ربط المنتج مع العلامات التجارية
    brands = models.ForeignKey(
        'Brand',  # تأكد أن لديك نموذج Brand موجود
        on_delete=models.CASCADE,  # يمكنك تحديد سياسة الحذف المناسبة
        related_name='products',
        blank=True,
        null=True  # إذا كنت تريد أن يكون الحقل اختياريًا
    )

    def __str__(self):
        return self.title

# جدول صور المنتج
class ProductPhoto(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='product_photos/')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Photo for {self.product.title}"

# جدول طلب المنتج
class RequestProduct(models.Model):

    STATUS_CHOICES = [
        ('new', 'جديد'),
        ('in_progress', 'تحت المعالجة'),
        ('resolved', 'تم الحل'),
        ('closed', 'مغلق'),
    ]
    file_types = models.ForeignKey(
        "FileType", 
        on_delete=models.SET_NULL,  # إذا تم حذف النوع، لا نحذف ملفات PDF
        null=True, 
        blank=True,
        related_name='pdfsss'
    )


    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField( null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='new'
    )  # حقل الحالة الجديد
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name





















# class SectionHeader(models.Model):
#     SECTION_TYPE_CHOICES = [
#     ('text', 'Text'),
#     ('image', 'Image'),
#     ('video', 'Video'),
#     ('slider', 'Slider'),
#     ('contact', 'Contact'),
#     ('project', 'Project'),
#     ('brand', 'Brand'),
#     ('service', 'Service'),
#     ('blog', 'Blog'),
#     ('testimonial', 'Testimonial'),
#     ('product', 'Product'),
#     ('about', 'About'),
#     ('feedback', 'Feedback')  ]
    
#     section_type = models.CharField(max_length=225, choices=SECTION_TYPE_CHOICES, null=True, blank=True)
#     title = models.CharField(max_length=255, null=True, blank=True)
 
#      # حقل TextField لتخزين HTML
#     html_content = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return self.title or "Section Header"
    





class GlobalInfo(models.Model):
    welcome_message = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=500, null=True, blank=True)
    whats_phone = models.CharField(max_length=500, null=True, blank=True)
    whats_product_massage = models.CharField(max_length=500, null=True, blank=True)
    whats_product_botton = models.CharField(max_length=500, null=True, blank=True)



    whats_home_massage = models.CharField(max_length=500, null=True, blank=True)



    email = models.EmailField(null=True, blank=True)
    logo_home = models.ImageField(upload_to='logos/', null=True, blank=True)
    micro_logo = models.ImageField(upload_to='micro_logos/', null=True, blank=True)
    svg_logo = models.FileField(upload_to='svg_logos/', null=True, blank=True)
    small_description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    html_content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.welcome_message or "Global Info"
    


class global_txt(models.Model):
    Send_message = models.CharField(max_length=200, null=True, blank=True)
    conect_us = models.CharField(max_length=200, null=True, blank=True)
    View_Project = models.CharField(max_length=200, null=True, blank=True)
    next_Projects = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    Brands = models.CharField(max_length=200, null=True, blank=True)
    bkcolor = models.CharField(max_length=200, null=True, blank=True)


    description = models.CharField(max_length=200, null=True, blank=True)
    Request = models.CharField(max_length=500, null=True, blank=True)
    details = models.CharField(max_length=200, null=True, blank=True)


    brand_title_section = models.CharField(max_length=500, null=True, blank=True)



    faq_img = models.ImageField(upload_to='faq_img/', null=True, blank=True)

    toast_massage_form_product = models.CharField(max_length=500, null=True, blank=True)



    def __str__(self):
        return self.Send_message or "Global global_txt"
    





class CompanyAddress(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    sub_title = models.CharField(max_length=500, null=True, blank=True)
    phone = models.CharField(max_length=500, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_footer = models.BooleanField(default=True)

    def __str__(self):
        return self.title or "Company Address"
    

    














class Pages(models.Model):
    title = models.CharField(max_length=255)
    is_default = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.title


class Sections(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class PagesStructer(models.Model):
    title = models.CharField(max_length=255,blank=True, null=True)


    pages = models.ForeignKey(Pages, on_delete=models.CASCADE, related_name='structures')
    sections = models.ForeignKey(Sections, on_delete=models.CASCADE, related_name='structures',blank=True, null=True)
    order = models.IntegerField(null=True, blank=True)  # عدد السكان
     # حقل TextField لتخزين HTML
    html_content = models.TextField(blank=True, null=True)
    command_code = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.pages} - {self.sections} -  {self.order} -   "
    













class Job(models.Model):
    JOB_STATUS_CHOICES = [
        ('open', 'مفتوح'),
        ('closed', 'مغلق'),
        ('pending', 'معلق'),
    ]





    title = models.CharField(max_length=255, verbose_name='العنوان')
    description = models.TextField(verbose_name='الوصف')

    html_content = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)



    status = models.CharField(
        max_length=10,
        choices=JOB_STATUS_CHOICES,
        default='open',
        verbose_name='الحالة'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')

    def __str__(self):
        return self.title
    


















class FileType(models.Model):
    name = models.CharField(max_length=100, unique=True)  # اسم النوع (مثل "User Manual")
    description = models.TextField(blank=True, null=True)  # وصف اختياري لنوع الملف

    def __str__(self):
        return self.name







class ProductPDF(models.Model):
    product = models.ForeignKey(
        Product, 
        on_delete=models.CASCADE,  
        related_name='pdfs'  
    )
    title = models.CharField(max_length=255, help_text="العنوان الذي سيظهر للمستخدم")  
    file_type = models.ForeignKey(
        FileType, 
        on_delete=models.SET_NULL,  # إذا تم حذف النوع، لا نحذف ملفات PDF
        null=True, 
        blank=True,
        related_name='pdfs'
    )
    file = models.FileField(upload_to='product_pdfs/')  
    uploaded_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.title} ({self.file_type.name if self.file_type else 'No Type'})"
