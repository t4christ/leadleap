from django.conf.urls import url
from django.contrib import admin

from ldtkc.views import auth_register,report,del_question,load_question,register_user,login_view,auth_logout,dashboard,test_dashboard,course_detail,user_test,take_test,submit_test,download_excel_data
urlpatterns =[


    url(r'^$',auth_register, name='home'),
    url(r'^get_registered/$', register_user, name='register_user'),
    url(r'^online_test/$', user_test, name='online_test'),
    # url(r'^populate/$', populate, name='online_test'),
    url(r'^submit_test/(?P<username>\w+)/$', submit_test, name='submit_test'),
    url(r'^test/(?P<username>\w+)_testdashboard$', test_dashboard, name='take_test'),
    url(r'^test/(?P<username>\w+)$', take_test, name='take_test'),
    url(r'^report/(?P<username>\w+)$', report, name='report'),
    url(r'^generate_report/(?P<username>\w+)$', download_excel_data, name='get_excel'),
    url(r'^login/$', login_view, name='login'),
    url(r'^logout/$', auth_logout, name='logout'),
    url(r'^(?P<username>\w+)_dashboard/$', dashboard, name='dashboard'),
    url(r'^(?P<username>\w+)/(?P<course_title>\w+)/$', course_detail, name='course_detail'),
    url(r'^qloads/$',load_question, name='load_question'),
    url(r'^dload/$', del_question, name='del_question'),

    # url(r'^(?P<username>\w+)/student_profile/$', student_profile, name='student_profile'),
    #url(r'^(?P<username>\w+)/edit_profile/$', edit_profile, name='edit_profile'),
    # url(r'^(?P<username>\w+)/edit_studentprofile/$', edit_studentprofile, name='edit_studentprofile'),
    ]
