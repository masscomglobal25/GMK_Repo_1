from django.urls import path, re_path as url
from app_send_mail import views

urlpatterns = [
    path('AdvertiserResetPassword/', views.advertiserResetPassword),
    path('AdvertiserVerifyAccount/', views.advertiserVerifyAccount),
    path('AdvertiserSignUpSuccess/', views.advertiserSignUpSuccess),
    path('AdvertiserSignUpSuccessToAdmin/', views.advertiserSignUpSuccessToAdmin),

    path('PublisherResetPassword/', views.publisherResetPassword),
    path('PublisherVerifyAccount/', views.publisherVerifyAccount),
    path('PublisherSignUpSuccess/', views.publisherSignUpSuccess),
    path('PublisherSignUpSuccessToAdmin/', views.publisherSignUpSuccessToAdmin),
    
    path('planCreatedByAdvertiser/', views.planCreatedByAdvertiser),
    path('planCreatedWithPremiumSupportByAdvertiser/', views.planCreatedWithPremiumSupportByAdvertiser),
    path('planCreatedWithPremiumSupportByAdvertiserToAdmin/', views.planCreatedWithPremiumSupportByAdvertiserToAdmin),
    path('planSendForApprovalForAdvertiser/', views.planSendForApprovalForAdvertiser),
    path('planSendForApprovalForPublisher/', views.planSendForApprovalForPublisher),
    path('planSendForApprovalForAdmin/', views.planSendForApprovalForAdmin),

    path('planApprovedByPublisherForAdvertiser/', views.planApprovedByPublisherForAdvertiser),
    path('PlanBookingConfirmedByAdvertiserToAdvertiser/', views.PlanBookingConfirmedByAdvertiserToAdvertiser),
    path('PlanBookingConfirmedByAdvertiserToAdmin/', views.PlanBookingConfirmedByAdvertiserToAdmin),
    path('PlanBookingConfirmedByAdvertiserForPublisher/', views.PlanBookingConfirmedByAdvertiserForPublisher),
    path('PlanBookedSucessfullyToAdvertiser/', views.PlanBookedSucessfullyToAdvertiser),

    path('PlanBookingCancelledByAdvertiserToAdmin/', views.PlanBookingCancelledByAdvertiserToAdmin),
    path('PlanBookingCancelledByAdvertiserToAdvertiser/', views.PlanBookingCancelledByAdvertiserToAdvertiser),


    path('MediaApprovalSubmittedForPublisher/', views.MediaApprovalSubmittedForPublisher),
    path('MediaRejectedByAdminForPublisher/', views.MediaRejectedByAdminForPublisher),
    path('MediaApprovedByAdminForPublisher/', views.MediaApprovedByAdminForPublisher),
    path('MediaActivatesByAdminForPublisher/', views.MediaActivatesByAdminForPublisher),
    path('MediaAdUintApprovalSubmittedForPublisher/', views.MediaAdUintApprovalSubmittedForPublisher),
    path('MediaAdUintApprovalSubmittedForAdmin/', views.MediaAdUintApprovalSubmittedForAdmin),
    # path('MediaAdUnitActivatesByAdminForPublisher/', views.MediaAdUnitActivatesByAdminForPublisher),
    # path('MediaAdUnitRejectedByAdminForPublisher/', views.MediaAdUnitRejectedByAdminForPublisher),
    path('MediaApprovalSubmittedForAdmin/', views.MediaApprovalSubmittedForAdmin),

    path('MeetingRequestByAdvertiserForAdmin/', views.MeetingRequestByAdvertiserForAdmin),
    path('MeetingRequestByAdvertiserForAdvertiser/', views.MeetingRequestByAdvertiserForAdvertiser),
    path('MeetingRequestByPublisherForAdmin/', views.MeetingRequestByPublisherForAdmin),
    path('MeetingRequestByPublisherForPublisher/', views.MeetingRequestByPublisherForPublisher),

    path('CreditRequestByAdvertiserForAdmin/', views.CreditRequestByAdvertiserForAdmin),
    path('CreditRequestByAdvertiserForAdvertiser/', views.CreditRequestByAdvertiserForAdvertiser),
    path('CreditRequestProceedByAdminForAdvertiser/', views.CreditRequestProceedByAdminForAdvertiser),
    

    path('testmail/', views.sendTestMail),

]
