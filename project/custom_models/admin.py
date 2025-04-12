from django.contrib import admin

from import_export import resources
from import_export.admin import ExportMixin,ImportMixin

from .models import (
    Slider, Service, Contact, Banner, Feedback, Testimonial, Category,
    Brand, Blog, BlogContent, Project, ProjectPhoto,
    AboutSection, Product, ProductPhoto, RequestProduct,
     GlobalInfo, CompanyAddress,Pages,Sections,PagesStructer,Job,global_txt
)

from .models import  ProductPDF, FileType

# تسجيل النماذج الخاصة بك في لوحة التحكم
# admin.site.register(Slider)
# admin.site.register(Service)
admin.site.register(Contact)
admin.site.register(Banner)



admin.site.register(ProductPDF)
admin.site.register(FileType)


# admin.site.register(Feedback)
# admin.site.register(Testimonial)
# admin.site.register(Category)
# admin.site.register(Brand)
# admin.site.register(Blog)
# admin.site.register(BlogContent)
# admin.site.register(Project)
# admin.site.register(ProjectPhoto)
# admin.site.register(Job)


# admin.site.register(AboutSection)
# admin.site.register(Product)
# admin.site.register(ProductPhoto)
admin.site.register(RequestProduct)
# admin.site.register(GlobalInfo)
# admin.site.register(CompanyAddress)

# admin.site.register(global_txt)


# admin.site.register(Pages)
# admin.site.register(Sections)
# admin.site.register(PagesStructer)







# class CategoryResource(resources.ModelResource):
#     class Meta:
#         model = Category

# class CategoryAdmin(ExportMixin, admin.ModelAdmin):
#     resource_class = CategoryResource

# admin.site.register(Category, CategoryAdmin)







# class CategoryResource(resources.ModelResource):
#     class Meta:
#         model = Category




# class CategoryAdmin(ImportMixin, ExportMixin, admin.ModelAdmin):
#     # إعدادات أخرى مثل قائمة الفلاتر أو القوائم


#     list_display = ('name', 'sub_title', 'description', 'is_active', 'visit_count')


# admin.site.register(Category, CategoryAdmin)








# تعريف الـ Admin للعلامات التجارية
class CategoryAdmin(ImportMixin, ExportMixin, admin.ModelAdmin):
    list_display = ('name', 'sub_title', 'description', 'is_active', 'visit_count')

# تسجيل العلامة التجارية في واجهة الادارة
admin.site.register(Category, CategoryAdmin)



















# تعريف Resource للعلامات التجارية
class BrandResource(resources.ModelResource):
    class Meta:
        model = Brand
        fields = ('id', 'name', 'sub_title', 'description', 'logo', 'is_active', 'categories')  # تحديد الحقول المسموح بها للاستيراد والتصدير

# تعريف الـ Admin للعلامات التجارية
class BrandAdmin(ImportMixin, ExportMixin, admin.ModelAdmin):
    list_display = ('name', 'sub_title', 'description', 'is_active', 'categories')  # عرض الحقول في واجهة الادارة
    list_filter = ('is_active', 'categories')  # فلترة العلامات التجارية حسب النشاط والفئات
    search_fields = ('name', 'description')  # إمكانية البحث حسب الاسم والوصف

# تسجيل العلامة التجارية في واجهة الادارة
admin.site.register(Brand, BrandAdmin)















# تعريف Resource للمنتجات
class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        fields = ('id', 'title', 'sub_title', 'description', 'details', 'in_home', 'is_active', 'categories', 'brands')  # الحقول التي سيتم استيرادها أو تصديرها

# تعريف Resource لصور المنتجات
class ProductPhotoResource(resources.ModelResource):
    class Meta:
        model = ProductPhoto
        fields = ('id', 'product', 'photo', 'is_main', 'is_active')  # الحقول التي سيتم استيرادها أو تصديرها

# تعريف الـ Admin للمنتجات
class ProductAdmin(ImportMixin, ExportMixin, admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'description', 'is_active', 'categories', 'brands')  # الحقول التي ستظهر في واجهة الإدارة
    list_filter = ('is_active', 'categories', 'brands')  # فلترة المنتجات حسب النشاط والفئات والعلامات التجارية
    search_fields = ('title', 'description')  # البحث حسب العنوان والوصف
    # إزالة filter_horizontal لأنها لا تعمل مع ForeignKey (فقط مع ManyToMany)
    # يمكنك استخدام filter_vertical إذا أردت عرض الفئات والعلامات التجارية بشكل عمودي
    # filter_horizontal = ('categories', 'brands')  # هذه السطر يتم إزالته أو استخدام filter_vertical بدلاً منها

# تعريف الـ Admin لصور المنتجات
class ProductPhotoAdmin(ImportMixin, ExportMixin, admin.ModelAdmin):
    list_display = ('product', 'photo', 'is_main', 'is_active')  # الحقول التي ستظهر في واجهة الإدارة
    list_filter = ('is_active', 'is_main')  # فلترة الصور حسب النشاط وهل هي الصورة الرئيسية
    search_fields = ('product__title',)  # البحث حسب عنوان المنتج

# تسجيل الـ Admin للمنتجات
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductPhoto, ProductPhotoAdmin)
















# تعريف الـ Admin للسلايدر
class SliderAdmin(ImportMixin, ExportMixin, admin.ModelAdmin):
    list_display = ('slider_type', 'title', 'sub_title', 'is_active')  # عرض الحقول في واجهة الادارة
    list_filter = ('slider_type', 'is_active')  # فلترة السلايدرات حسب النوع والنشاط
    search_fields = ('title', 'sub_title')  # إمكانية البحث حسب العنوان والعنوان الفرعي


# تسجيل السلايدر في واجهة الادارة
admin.site.register(Slider, SliderAdmin)















# تعريف الـ Admin للخدمات
class ServiceAdmin(ImportMixin, ExportMixin, admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'overview', 'active')  # عرض الحقول في واجهة الادارة
    list_filter = ('active',)  # فلترة الخدمات حسب النشاط
    search_fields = ('title', 'sub_title', 'overview')  # إمكانية البحث حسب العنوان والعنوان الفرعي والنظرة العامة

# تسجيل الخدمة في واجهة الادارة
admin.site.register(Service, ServiceAdmin)













# تعريف الـ Admin للتعليقات
class FeedbackAdmin(ImportMixin, ExportMixin, admin.ModelAdmin):
    list_display = ('title', 'icon', 'number', 'is_active')  # عرض الحقول في واجهة الادارة
    list_filter = ('is_active',)  # فلترة التعليقات حسب النشاط
    search_fields = ('title', 'icon')  # إمكانية البحث حسب العنوان والرمز

# تسجيل التعليق في واجهة الادارة
admin.site.register(Feedback, FeedbackAdmin)













# تعريف الـ Admin للتوصيات
class TestimonialAdmin(ImportMixin, ExportMixin, admin.ModelAdmin):
    list_display = ('name', 'position', 'quote', 'is_active')  # عرض الحقول في واجهة الادارة
    list_filter = ('is_active',)  # فلترة التوصيات حسب النشاط
    search_fields = ('name', 'quote')  # إمكانية البحث حسب الاسم والاقتباس

# تسجيل التوصية في واجهة الادارة
admin.site.register(Testimonial, TestimonialAdmin)














# تعريف الـ Admin للمدونات
class BlogAdmin(ImportMixin, ExportMixin, admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'created_at', 'is_active', 'categories')  # عرض الحقول في واجهة الادارة
    list_filter = ('is_active', 'categories')  # فلترة المدونات حسب النشاط والفئات
    search_fields = ('title', 'sub_title')  # البحث حسب العنوان والعنوان الفرعي

# تعريف الـ Admin لمحتوى المدونات
class BlogContentAdmin(ImportMixin, ExportMixin, admin.ModelAdmin):
    list_display = ('header', 'blog', 'ordering', 'is_active')  # عرض الحقول في واجهة الادارة
    list_filter = ('is_active', 'ordering')  # فلترة محتوى المدونة حسب النشاط والترتيب
    search_fields = ('header', 'content')  # البحث حسب العنوان والمحتوى

# تسجيل المدونة ومحتوى المدونة في واجهة الادارة
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogContent, BlogContentAdmin)















# تعريف الـ Admin للمشاريع
class ProjectAdmin(ImportMixin, ExportMixin, admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'year', 'project_type', 'is_active')  # عرض الحقول في واجهة الادارة
    list_filter = ('is_active', 'project_type')  # فلترة المشاريع حسب النشاط ونوع المشروع
    search_fields = ('title', 'project_type')  # البحث حسب العنوان ونوع المشروع

# تعريف الـ Admin لصور المشاريع
class ProjectPhotoAdmin(ImportMixin, ExportMixin, admin.ModelAdmin):
    list_display = ('project', 'photo', 'in_header', 'is_active')  # عرض الحقول في واجهة الادارة
    list_filter = ('is_active', 'in_header')  # فلترة صور المشاريع حسب النشاط وهل هي الصورة الرئيسية
    search_fields = ('project__title',)  # البحث حسب عنوان المشروع

# تسجيل المشاريع وصور المشاريع في واجهة الادارة
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectPhoto, ProjectPhotoAdmin)















# تعريف الـ Admin للقسم
class AboutSectionAdmin(ImportMixin, ExportMixin, admin.ModelAdmin):
    list_display = ('title', 'if_about_page', 'video', 'type', 'is_active')  # عرض الحقول في واجهة الادارة
    list_filter = ('is_active', 'type')  # فلترة الأقسام حسب النشاط ونوع المحتوى
    search_fields = ('title',)  # البحث حسب العنوان

 
# تسجيل القسم ومحتوى القسم في واجهة الادارة
admin.site.register(AboutSection, AboutSectionAdmin)
 
















# تعريف الـ Admin لـ GlobalInfo
class GlobalInfoAdmin(ImportMixin, ExportMixin, admin.ModelAdmin):
    list_display = ('welcome_message', 'phone', 'email', 'is_active')  # عرض الحقول في واجهة الادارة
    list_filter = ('is_active',)  # فلترة حسب النشاط
    search_fields = ('welcome_message', 'phone', 'email')  # البحث حسب الرسالة الترحيبية، الهاتف، والبريد الإلكتروني

# تسجيل GlobalInfo في واجهة الادارة
admin.site.register(GlobalInfo, GlobalInfoAdmin) 







# تعريف الـ Admin لـ global_txt
class GlobalTxtAdmin(ImportMixin, ExportMixin, admin.ModelAdmin):
    list_display = ('Send_message', 'conect_us', 'View_Project', 'next_Projects')  # عرض الحقول في واجهة الإدارة
    list_filter = ('Send_message',)  # فلترة حسب الرسالة
    search_fields = ('Send_message', 'conect_us', 'View_Project', 'next_Projects')  # البحث حسب الحقول

# تسجيل global_txt في واجهة الإدارة
admin.site.register(global_txt, GlobalTxtAdmin)








# تعريف الـ Admin لـ CompanyAddress
class CompanyAddressAdmin(ImportMixin, ExportMixin, admin.ModelAdmin):
    list_display = ('title', 'sub_title', 'phone', 'email', 'is_active', 'is_footer')  # عرض الحقول في واجهة الادارة
    list_filter = ('is_active', 'is_footer')  # فلترة حسب النشاط وهل يتم عرضه في الفوتر
    search_fields = ('title', 'phone', 'email')  # البحث حسب العنوان، الهاتف، والبريد الإلكتروني

# تسجيل CompanyAddress في واجهة الادارة
admin.site.register(CompanyAddress, CompanyAddressAdmin)












# تعريف Admin لـ Job
class JobAdmin(ImportMixin, ExportMixin, admin.ModelAdmin):
    list_display = ('title', 'status', 'is_active', 'created_at')  # عرض الحقول في واجهة الإدارة
    list_filter = ('status', 'is_active')  # فلترة حسب الحالة والنشاط
    search_fields = ('title', 'description')  # البحث حسب العنوان والوصف

# تسجيل Job في واجهة الإدارة
admin.site.register(Job, JobAdmin)










# تعريف الـ Admin لـ Pages
class PagesAdmin(ImportMixin, ExportMixin, admin.ModelAdmin):
    list_display = ('title', 'is_default')  # عرض الحقول في واجهة الادارة
    list_filter = ('is_default',)  # فلترة حسب ما إذا كان هو الافتراضي
    search_fields = ('title',)  # البحث حسب العنوان

# تعريف الـ Admin لـ Sections
class SectionsAdmin(ImportMixin, ExportMixin, admin.ModelAdmin):
    list_display = ('title',)  # عرض الحقول في واجهة الادارة
    search_fields = ('title',)  # البحث حسب العنوان

# تعريف الـ Admin لـ PagesStructer
class PagesStructerAdmin(ImportMixin, ExportMixin, admin.ModelAdmin):
    list_display = ('title', 'pages', 'sections', 'order', 'html_content', 'command_code')  # عرض الحقول في واجهة الادارة
    list_filter = ('pages', 'sections')  # فلترة حسب الصفحات والأقسام
    search_fields = ('title', 'html_content')  # البحث حسب العنوان والمحتوى

# تسجيل Pages في واجهة الادارة
admin.site.register(Pages, PagesAdmin)
# تسجيل Sections في واجهة الادارة
admin.site.register(Sections, SectionsAdmin)
# تسجيل PagesStructer في واجهة الادارة
admin.site.register(PagesStructer, PagesStructerAdmin)