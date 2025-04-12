from modeltranslation.translator import translator, TranslationOptions
from .models import AboutSection, Blog, BlogContent, Brand,FileType, Category, CompanyAddress, Feedback, GlobalInfo, Job, PagesStructer, Product, Project, Service, Slider, Testimonial, global_txt

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'sub_title','description')  # تحديد الحقول التي تريد ترجمتها

translator.register(Category, CategoryTranslationOptions)


class SliderTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title')
translator.register(Slider, SliderTranslationOptions)




# class SectionHeaderTranslationOptions(TranslationOptions):
#     fields = ('title','html_content' )
# translator.register(SectionHeader, SectionHeaderTranslationOptions)



class AboutSectionTranslationOptions(TranslationOptions):
    fields = ('title', 'html_content')
translator.register(AboutSection, AboutSectionTranslationOptions)


class FeedbackTranslationOptionss(TranslationOptions):
    fields = ('title','icon' )
translator.register(Feedback, FeedbackTranslationOptionss)







class PagesStructerTranslationOptionss(TranslationOptions):
    fields = ('html_content','title' )
translator.register(PagesStructer, PagesStructerTranslationOptionss)





class ServiceStructerTranslationOptionss(TranslationOptions):
    fields = ('title','sub_title' ,'overview','html_content')
translator.register(Service, ServiceStructerTranslationOptionss)





class ProjectStructerTranslationOptionss(TranslationOptions):
    fields = ('title','sub_title' ,'project_type','html_content')
translator.register(Project, ProjectStructerTranslationOptionss)




class TestimonialStructerTranslationOptionss(TranslationOptions):
    fields = ('name','position' ,'quote')
translator.register(Testimonial, TestimonialStructerTranslationOptionss)



class ProducttructerTranslationOptionss(TranslationOptions):
    fields = ('title','sub_title' ,'description','details')
translator.register(Product, ProducttructerTranslationOptionss)





class BlogTranslationOptionss(TranslationOptions):
    fields = ('title','sub_title' ,'html_content')
translator.register(Blog, BlogTranslationOptionss)



class BlogContentTranslationOptionss(TranslationOptions):
    fields = ('header','content' )
translator.register(BlogContent, BlogContentTranslationOptionss)



class CompanyAddressContentTranslationOptionss(TranslationOptions):
    fields = ('title','sub_title' )
translator.register(CompanyAddress, CompanyAddressContentTranslationOptionss)



class GlobalInfoContentTranslationOptionss(TranslationOptions):
    fields = ('welcome_message','small_description','html_content','whats_product_massage','whats_product_botton','whats_home_massage' )
translator.register(GlobalInfo, GlobalInfoContentTranslationOptionss)




class global_txtContentTranslationOptionss(TranslationOptions):
    fields = ('Send_message','conect_us','View_Project','next_Projects','category','Brands','description','Request','details' ,'brand_title_section','toast_massage_form_product')
translator.register(global_txt, global_txtContentTranslationOptionss)









class JobTranslationOptionss(TranslationOptions):
    fields = ('title','description','html_content' )
translator.register(Job, JobTranslationOptionss)






class BrandTranslationOptionss(TranslationOptions):
    fields = ('name','sub_title','description' )
translator.register(Brand, BrandTranslationOptionss)


class FileTypeTranslationOptionss(TranslationOptions):
    fields = ('name','description'  )
translator.register(FileType, FileTypeTranslationOptionss)

