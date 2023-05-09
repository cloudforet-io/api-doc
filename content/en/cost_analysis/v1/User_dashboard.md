---
title: "User_dashboard"
linkTitle: "User_dashboard"
weight: 3
bookFlatSection: true
---
# [User_dashboard](#User_dashboard)
A UserDashboard is a cost data dashboard customized with a combination of widgets a User want.


>  **Package : spaceone.api.cost_analysis.v1**

<br>
<br>

## User_dashboard





**UserDashboard Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./UserDashboard#create) | [CreateUserDashboardRequest](UserDashboard#createuserdashboardrequest) | [UserDashboardInfo](./UserDashboard#userdashboardinfo) |
| [**update**](./UserDashboard#update) | [UpdateUserDashboardRequest](UserDashboard#updateuserdashboardrequest) | [UserDashboardInfo](./UserDashboard#userdashboardinfo) |
| [**delete**](./UserDashboard#delete) | [UserDashboardRequest](UserDashboard#userdashboardrequest) | [Empty](./UserDashboard#empty) |
| [**get**](./UserDashboard#get) | [GetUserDashboardRequest](UserDashboard#getuserdashboardrequest) | [UserDashboardInfo](./UserDashboard#userdashboardinfo) |
| [**list**](./UserDashboard#list) | [UserDashboardQuery](UserDashboard#userdashboardquery) | [UserDashboardsInfo](./UserDashboard#userdashboardsinfo) |
| [**stat**](./UserDashboard#stat) | [UserDashboardStatQuery](UserDashboard#userdashboardstatquery) | [Struct](./UserDashboard#struct) |



    
<br>

### create

Creates a new UserDashboard. Users can use the dashboard in `private`. In addition to the widgets provided by Cloudforet by default, Users can use widgets through the CustomWidget resource to create a UserDashboard that suits their needs.



> **POST** /cost-analysis/v1/user-dashboard/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateUserDashboardRequest](./UserDashboard#createuserdashboardrequest)

* **name** (string)  `Required` 


* **domain_id** (string)  `Required` 


* **default_layout_id** (string) 


* **custom_layouts** (ListValue) 


* **default_filter** (Struct) 


* **period_type** (PeriodType) 


* **period** (UserDashboardPeriod) 


* **tags** (Struct) 





{{< highlight json >}}
{
   "name": "Untitled Dashboard",
   "custom_layouts": [
       [
           {
               "name": "AWS Data-Transfer Cost Trend",
               "widget_id": "linegraph-lg-02",
               "options": {
                   "layout": 100.0,
                   "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_DATA_TRANSFER_COST_TREND_DESC",
                   "chart_type": "LINE",
                   "chart_img": "AWS_Data-Transfer_Cost_Trend"
               }
           }
       ],
       [
           {
               "options": {
                   "chart_type": "MAP",
                   "chart_img": "AWS_Data-Transfer_By_Region",
                   "layout": 100.0,
                   "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_DATA_TRANSFER_BY_REGION_DESC"
               },
               "name": "AWS Data-Transfer by Region",
               "widget_id": "map-lg-02"
           }
       ],
       [
           {
               "options": {
                   "group_by": "project_id",
                   "layout": 100.0,
                   "chart_type": "STACKED_COLUMN",
                   "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_CLOUDFRONT_COST_DESC",
                   "chart_img": "AWS_CloudFront_Cost"
               },
               "name": "AWS CloudFront Cost by Project",
               "widget_id": "stackedcol-lg-03"
           }
       ]
   ],
   "default_filter": {},
   "period_type": "AUTO"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[UserDashboardInfo](#USERDASHBOARDINFO)
* **user_dashboard_id** (string)  `Required` 

* **name** (string)  `Required` 

* **default_layout_id** (string)  `Required` 

* **custom_layouts** (ListValue)  `Required` 

* **default_filter** (Struct)  `Required` 

* **period_type** (PeriodType)  `Required` 

* **period** (UserDashboardPeriod)  `Required` 

* **tags** (Struct)  `Required` 

* **user_id** (string)  `Required` 

* **domain_id** (string)  `Required` 

* **created_at** (string)  `Required` 

* **updated_at** (string)  `Required` 



{{< highlight json >}}
{
   "user_dashboard_id": "user-dash-bf3f5f5ffa03",
   "name": "Untitled Dashboard",
   "custom_layouts": [
       [
           {
               "options": {
                   "chart_type": "LINE",
                   "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_DATA_TRANSFER_COST_TREND_DESC",
                   "layout": 100.0,
                   "chart_img": "AWS_Data-Transfer_Cost_Trend"
               },
               "widget_id": "linegraph-lg-02",
               "name": "AWS Data-Transfer Cost Trend"
           }
       ],
       [
           {
               "name": "AWS Data-Transfer by Region",
               "widget_id": "map-lg-02",
               "options": {
                   "chart_img": "AWS_Data-Transfer_By_Region",
                   "chart_type": "MAP",
                   "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_DATA_TRANSFER_BY_REGION_DESC",
                   "layout": 100.0
               }
           }
       ],
       [
           {
               "widget_id": "stackedcol-lg-03",
               "name": "AWS CloudFront Cost by Project",
               "options": {
                   "layout": 100.0,
                   "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_CLOUDFRONT_COST_DESC",
                   "chart_img": "AWS_CloudFront_Cost",
                   "group_by": "project_id",
                   "chart_type": "STACKED_COLUMN"
               }
           }
       ]
   ],
   "default_filter": {},
   "period_type": "AUTO",
   "tags": {},
   "user_id": "seolmin@mz.co.kr",
   "domain_id": "domain-58010aa2e451",
   "created_at": "2022-07-19T05:58:52.065Z",
   "updated_at": "2022-07-19T05:58:52.065Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update

Updates a specific UserDashboard. You can make changes in widgets, including default widgets and CustomWidegets.



> **POST** /cost-analysis/v1/user-dashboard/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateUserDashboardRequest](./UserDashboard#updateuserdashboardrequest)

* **user_dashboard_id** (string)  `Required` 


* **domain_id** (string)  `Required` 


* **name** (string) 


* **default_layout_id** (string) 


* **custom_layouts** (ListValue) 


* **default_filter** (Struct) 


* **period_type** (PeriodType) 


* **period** (UserDashboardPeriod) 


* **tags** (Struct) 





{{< highlight json >}}
{
   "user_dashboard_id": "user-dash-bf3f5f5ffa03",
   "name": "Untitled Dashboard2",
   "custom_layouts": [
       [{
           "options": {
               "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_DATA_TRANSFER_COST_TREND_DESC",
               "chart_type": "LINE", "chart_img": "AWS_Data-Transfer_Cost_Trend", "layout": 100.0},
           "name": "AWS Data-Transfer Cost Trend",
           "widget_id": "linegraph-lg-02"}],
       [{
           "name": "AWS Data-Transfer by Region",
           "options": {
               "chart_type": "MAP",
               "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_DATA_TRANSFER_BY_REGION_DESC",
               "layout": 100.0,
               "chart_img": "AWS_Data-Transfer_By_Region"},
           "widget_id": "map-lg-02"}],
       [{
           "name": "AWS CloudFront Cost by Project",
           "widget_id": "stackedcol-lg-03",
           "options": {
               "layout": 100.0,
               "chart_img": "AWS_CloudFront_Cost",
               "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_CLOUDFRONT_COST_DESC",
               "chart_type": "STACKED_COLUMN",
               "group_by": "project_id"}
       }]
   ]
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[UserDashboardInfo](#USERDASHBOARDINFO)
* **user_dashboard_id** (string)  `Required` 

* **name** (string)  `Required` 

* **default_layout_id** (string)  `Required` 

* **custom_layouts** (ListValue)  `Required` 

* **default_filter** (Struct)  `Required` 

* **period_type** (PeriodType)  `Required` 

* **period** (UserDashboardPeriod)  `Required` 

* **tags** (Struct)  `Required` 

* **user_id** (string)  `Required` 

* **domain_id** (string)  `Required` 

* **created_at** (string)  `Required` 

* **updated_at** (string)  `Required` 



{{< highlight json >}}
{
   "user_dashboard_id": "user-dash-bf3f5f5ffa03",
   "name": "Untitled Dashboard",
   "custom_layouts": [
       [
           {
               "options": {
                   "chart_type": "LINE",
                   "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_DATA_TRANSFER_COST_TREND_DESC",
                   "layout": 100.0,
                   "chart_img": "AWS_Data-Transfer_Cost_Trend"
               },
               "widget_id": "linegraph-lg-02",
               "name": "AWS Data-Transfer Cost Trend"
           }
       ],
       [
           {
               "name": "AWS Data-Transfer by Region",
               "widget_id": "map-lg-02",
               "options": {
                   "chart_img": "AWS_Data-Transfer_By_Region",
                   "chart_type": "MAP",
                   "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_DATA_TRANSFER_BY_REGION_DESC",
                   "layout": 100.0
               }
           }
       ],
       [
           {
               "widget_id": "stackedcol-lg-03",
               "name": "AWS CloudFront Cost by Project",
               "options": {
                   "layout": 100.0,
                   "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_CLOUDFRONT_COST_DESC",
                   "chart_img": "AWS_CloudFront_Cost",
                   "group_by": "project_id",
                   "chart_type": "STACKED_COLUMN"
               }
           }
       ]
   ],
   "default_filter": {},
   "period_type": "AUTO",
   "tags": {},
   "user_id": "seolmin@mz.co.kr",
   "domain_id": "domain-58010aa2e451",
   "created_at": "2022-07-19T05:58:52.065Z",
   "updated_at": "2022-07-19T05:58:52.065Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete

Deletes a specific UserDashboard. You must specify the `user_dashboard_id` of the UserDashboard to delete.



> **POST** /cost-analysis/v1/user-dashboard/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[UserDashboardRequest](./UserDashboard#userdashboardrequest)

* **user_dashboard_id** (string)  `Required` 


* **domain_id** (string)  `Required` 





{{< highlight json >}}
{
   "user_dashboard_id": "user-dash-d1bd5d8cb6d7"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get

Gets a specific UserDashboard. Prints detailed information about the UserDashboard, including widegts used.



> **POST** /cost-analysis/v1/user-dashboard/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[GetUserDashboardRequest](./UserDashboard#getuserdashboardrequest)

* **user_dashboard_id** (string)  `Required` 


* **domain_id** (string)  `Required` 


* **only** (string) 





{{< highlight json >}}
{
   "user_dashboard_id": "user-dash-d1bd5d8cb6d7"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[UserDashboardInfo](#USERDASHBOARDINFO)
* **user_dashboard_id** (string)  `Required` 

* **name** (string)  `Required` 

* **default_layout_id** (string)  `Required` 

* **custom_layouts** (ListValue)  `Required` 

* **default_filter** (Struct)  `Required` 

* **period_type** (PeriodType)  `Required` 

* **period** (UserDashboardPeriod)  `Required` 

* **tags** (Struct)  `Required` 

* **user_id** (string)  `Required` 

* **domain_id** (string)  `Required` 

* **created_at** (string)  `Required` 

* **updated_at** (string)  `Required` 



{{< highlight json >}}
{
   "user_dashboard_id": "user-dash-bf3f5f5ffa03",
   "name": "Untitled Dashboard",
   "custom_layouts": [
       [
           {
               "options": {
                   "chart_type": "LINE",
                   "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_DATA_TRANSFER_COST_TREND_DESC",
                   "layout": 100.0,
                   "chart_img": "AWS_Data-Transfer_Cost_Trend"
               },
               "widget_id": "linegraph-lg-02",
               "name": "AWS Data-Transfer Cost Trend"
           }
       ],
       [
           {
               "name": "AWS Data-Transfer by Region",
               "widget_id": "map-lg-02",
               "options": {
                   "chart_img": "AWS_Data-Transfer_By_Region",
                   "chart_type": "MAP",
                   "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_DATA_TRANSFER_BY_REGION_DESC",
                   "layout": 100.0
               }
           }
       ],
       [
           {
               "widget_id": "stackedcol-lg-03",
               "name": "AWS CloudFront Cost by Project",
               "options": {
                   "layout": 100.0,
                   "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_CLOUDFRONT_COST_DESC",
                   "chart_img": "AWS_CloudFront_Cost",
                   "group_by": "project_id",
                   "chart_type": "STACKED_COLUMN"
               }
           }
       ]
   ],
   "default_filter": {},
   "period_type": "AUTO",
   "tags": {},
   "user_id": "seolmin@mz.co.kr",
   "domain_id": "domain-58010aa2e451",
   "created_at": "2022-07-19T05:58:52.065Z",
   "updated_at": "2022-07-19T05:58:52.065Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Gets a list of all UserDashboards. You can use a query to get a filtered list of UserDashboards.



> **POST** /cost-analysis/v1/user-dashboard/list
>





 {{< tabs " list " >}}



 {{< tab "Response Example" >}}

[UserDashboardsInfo](#USERDASHBOARDSINFO)
* **results** (UserDashboardInfo)  `Required` 

* **total_count** (int32)  `Required` 



{{< highlight json >}}
{
   "results": [
       {
           "user_dashboard_id": "user-dash-d1bd5d8cb6d7",
           "name": "11 Months Public Cloud Cost Summary",
           "custom_layouts": [
               [
                   {
                       "options": {
                           "layout": 100.0,
                           "chart_type": "CARD"
                       },
                       "widget_id": "card-lg-01",
                       "name": "Budget Usage Summary"
                   }
               ],
               [
                   {
                       "name": "Project-wise Budget Usage Summary@@",
                       "options": {
                           "chart_type": "TABLE",
                           "layout": 100.0
                       },
                       "widget_id": "table-lg-01"
                   }
               ],
               [
                   {
                       "widget_id": "stackedcol-lg-02",
                       "options": {
                           "layout": 100.0,
                           "group_by": "product",
                           "chart_type": "STACKED_COLUMN"
                       },
                       "name": "Cost Trend By Product"
                   }
               ]
           ],
           "default_filter": {
               "project_id": []
           },
           "period_type": "FIXED",
           "period": {
               "start": "2021-04-01",
               "end": "2022-02-28"
           },
           "tags": {},
           "user_id": "wanzargen@mz.co.kr",
           "domain_id": "domain-58010aa2e451",
           "created_at": "2022-03-03T03:36:35.396Z",
           "updated_at": "2022-03-03T03:36:35.396Z"
       },
       {
           "user_dashboard_id": "user-dash-965b03793d5b",
           "name": "AWS CloudFront Cost by Project",
           "custom_layouts": [
               [
                   {
                       "name": "AWS CloudFront Cost by Project",
                       "widget_id": "stackedcol-lg-03",
                       "options": {
                           "chart_type": "STACKED_COLUMN",
                           "layout": 100.0
                       }
                   }
               ],
               [
                   {
                       "widget_id": "stackedcol-lg-03",
                       "options": {
                           "layout": 100.0,
                           "chart_type": "STACKED_COLUMN",
                           "group_by": "service_account_id"
                       },
                       "name": "AWS CloudFront Cost by Service Account"
                   }
               ],
               [
                   {
                       "options": {
                           "layout": 100.0,
                           "chart_type": "LINE"
                       },
                       "name": "AWS Data-Transfer Cost Trend",
                       "widget_id": "linegraph-lg-02"
                   }
               ]
           ],
           "default_filter": {},
           "period_type": "FIXED",
           "period": {
               "start": "2021-05-01",
               "end": "2022-04-30"
           },
           "tags": {},
           "user_id": "wanzargen@mz.co.kr",
           "domain_id": "domain-58010aa2e451",
           "created_at": "2022-04-07T01:13:28.494Z",
           "updated_at": "2022-04-07T01:13:28.494Z"
       }
   ],
   "total_count": 48
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /cost-analysis/v1/user-dashboard/stat
>






    


<br>
<br>

## Message



### CreateUserDashboardRequest
* **name** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **default_layout_id** (string) 

    
* **custom_layouts** (ListValue) 

    
* **default_filter** (Struct) 

    
* **period_type** (PeriodType) 

    
* **period** (UserDashboardPeriod) 

    
* **tags** (Struct) 

    <br>

### GetUserDashboardRequest
* **user_dashboard_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **only** (string) 

    <br>

### UpdateUserDashboardRequest
* **user_dashboard_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **name** (string) 

    
* **default_layout_id** (string) 

    
* **custom_layouts** (ListValue) 

    
* **default_filter** (Struct) 

    
* **period_type** (PeriodType) 

    
* **period** (UserDashboardPeriod) 

    
* **tags** (Struct) 

    <br>

### UserDashboardInfo
* **user_dashboard_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **default_layout_id** (string)  `Required` 

    
* **custom_layouts** (ListValue)  `Required` 

    
* **default_filter** (Struct)  `Required` 

    
* **period_type** (PeriodType)  `Required` 

    
* **period** (UserDashboardPeriod)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **user_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **updated_at** (string)  `Required` 

    <br>

### UserDashboardPeriod
* **start** (string)  `Required` 

    
* **end** (string)  `Required` 

    <br>

### UserDashboardQuery
* **domain_id** (string)  `Required` 

    
* **query** (Query) 

    
* **user_dashboard_id** (string) 

    
* **name** (string) 

    
* **period_type** (PeriodType) 

    
* **user_id** (string) 

    <br>

### UserDashboardRequest
* **user_dashboard_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### UserDashboardStatQuery
* **query** (StatisticsQuery)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### UserDashboardsInfo
* **results** (UserDashboardInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>
