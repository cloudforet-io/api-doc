---
title: "PublicDashboard"
linkTitle: "PublicDashboard"
weight: 3
bookFlatSection: true
---
# [PublicDashboard](#PublicDashboard)
A PublicDashboard is a cost data dashboard provided to all users by default.


>  **Package : spaceone.api.cost_analysis.v1**

<br>
<br>

## PublicDashboard





**PublicDashboard Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./PublicDashboard#create) | [CreatePublicDashboardRequest](PublicDashboard#createpublicdashboardrequest) | [PublicDashboardInfo](./PublicDashboard#publicdashboardinfo) |
| [**update**](./PublicDashboard#update) | [UpdatePublicDashboardRequest](PublicDashboard#updatepublicdashboardrequest) | [PublicDashboardInfo](./PublicDashboard#publicdashboardinfo) |
| [**delete**](./PublicDashboard#delete) | [PublicDashboardRequest](PublicDashboard#publicdashboardrequest) | [Empty](./PublicDashboard#empty) |
| [**get**](./PublicDashboard#get) | [GetPublicDashboardRequest](PublicDashboard#getpublicdashboardrequest) | [PublicDashboardInfo](./PublicDashboard#publicdashboardinfo) |
| [**list**](./PublicDashboard#list) | [PublicDashboardQuery](PublicDashboard#publicdashboardquery) | [PublicDashboardsInfo](./PublicDashboard#publicdashboardsinfo) |
| [**stat**](./PublicDashboard#stat) | [PublicDashboardStatQuery](PublicDashboard#publicdashboardstatquery) | [Struct](./PublicDashboard#struct) |



    
<br>

### create

Creates a new PublicDashboard. This method is used for creating the default dashboard . `Admin` type Users can use the method to add a new dashboard with customized widgets.



> **POST** /cost-analysis/v1/public-dashboard/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreatePublicDashboardRequest](./PublicDashboard#createpublicdashboardrequest)

* **name** (string)  `Required` 


* **domain_id** (string)  `Required` 


* **default_layout_id** (string) 


* **custom_layouts** (ListValue) 


* **default_filter** (Struct) 


* **period_type** (PeriodType) 


* **period** (PublicDashboardPeriod) 


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
                   "chart_type": "LINE",
                   "layout": 100.0,
                   "chart_img": "AWS_Data-Transfer_Cost_Trend",
                   "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_DATA_TRANSFER_COST_TREND_DESC"
               }
            }
        ],
        [
           {
               "name": "AWS Data-Transfer by Region",
               "widget_id": "map-lg-02",
               "options": {
                   "chart_type": "MAP", "layout": 100.0,
                   "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_DATA_TRANSFER_BY_REGION_DESC",
                   "chart_img": "AWS_Data-Transfer_By_Region"
               }
           }
       ],
       [
           {
               "name": "AWS CloudFront Cost by Project",
               "widget_id": "stackedcol-lg-03",
               "options": {
                   "group_by": "project_id",
                   "chart_img": "AWS_CloudFront_Cost",
                   "layout": 100.0,
                   "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_CLOUDFRONT_COST_DESC",
                   "chart_type": "STACKED_COLUMN"
               }
           }
       ]
   ],
   "default_filter": {},
   "period_type": "AUTO"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[PublicDashboardInfo](#PUBLICDASHBOARDINFO)
* **public_dashboard_id** (string)  `Required` 

* **name** (string)  `Required` 

* **default_layout_id** (string)  `Required` 

* **custom_layouts** (ListValue)  `Required` 

* **default_filter** (Struct)  `Required` 

* **period_type** (PeriodType)  `Required` 

* **period** (PublicDashboardPeriod)  `Required` 

* **tags** (Struct)  `Required` 

* **domain_id** (string)  `Required` 

* **created_at** (string)  `Required` 

* **updated_at** (string)  `Required` 



{{< highlight json >}}
{
   "public_dashboard_id": "pub-dash-80092b5ef658",
   "name": "Untitled Dashboard",
   "custom_layouts": [
       [
           {
               "options": {
                   "layout": 100.0,
                   "chart_type": "LINE",
                   "chart_img": "AWS_Data-Transfer_Cost_Trend",
                   "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_DATA_TRANSFER_COST_TREND_DESC"
               },
               "widget_id": "linegraph-lg-02",
               "name": "AWS Data-Transfer Cost Trend"
           }
       ],
       [
           {
               "widget_id": "map-lg-02",
               "name": "AWS Data-Transfer by Region",
               "options": {
                   "layout": 100.0,
                   "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_DATA_TRANSFER_BY_REGION_DESC",
                   "chart_img": "AWS_Data-Transfer_By_Region",
                   "chart_type": "MAP"
               }
           }
       ],
       [
           {
               "options": {
                   "chart_type": "STACKED_COLUMN",
                   "chart_img": "AWS_CloudFront_Cost",
                   "layout": 100.0,
                   "group_by": "project_id",
                   "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_CLOUDFRONT_COST_DESC"
               },
               "name": "AWS CloudFront Cost by Project",
               "widget_id": "stackedcol-lg-03"
           }
       ]
   ],
   "default_filter": {},
   "period_type": "AUTO",
   "tags": {},
   "domain_id": "domain-58010aa2e451",
   "created_at": "2022-07-19T05:42:01.412Z",
   "updated_at": "2022-07-19T05:42:01.412Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update

Updates a specific PublicDashboard. Changes the widgets of the PublicDashboard with default widgets and customized widgets. Only `Admin` type Users can use the method.



> **POST** /cost-analysis/v1/public-dashboard/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdatePublicDashboardRequest](./PublicDashboard#updatepublicdashboardrequest)

* **public_dashboard_id** (string)  `Required` 


* **domain_id** (string)  `Required` 


* **name** (string) 


* **default_layout_id** (string) 


* **custom_layouts** (ListValue) 


* **default_filter** (Struct) 


* **period_type** (PeriodType) 


* **period** (PublicDashboardPeriod) 


* **tags** (Struct) 





{{< highlight json >}}
{
   "public_dashboard_id": "pub-dash-80092b5ef658",
   "name": "Untitled Dashboard2",
   "custom_layouts": [
       [
           {
               "widget_id": "linegraph-lg-02",
               "name": "AWS Data-Transfer Cost Trend",
               "options": {
                   "chart_type": "LINE",
                   "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_DATA_TRANSFER_COST_TREND_DESC",
                   "chart_img": "AWS_Data-Transfer_Cost_Trend",
                   "layout": 100.0
               }
           }
       ],
       [
           {
               "name": "AWS Data-Transfer by Region",
               "widget_id": "map-lg-02",
               "options": {
                   "chart_type": "MAP",
                   "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_DATA_TRANSFER_BY_REGION_DESC",
                   "layout": 100.0,
                   "chart_img": "AWS_Data-Transfer_By_Region"
               }
           }
       ],
       [
           {
               "name": "AWS CloudFront Cost by Project",
               "widget_id": "stackedcol-lg-03",
               "options": {
                   "layout": 100.0,
                   "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_CLOUDFRONT_COST_DESC",
                   "group_by": "project_id",
                   "chart_type": "STACKED_COLUMN",
                   "chart_img": "AWS_CloudFront_Cost"
               }
           }
       ]
   ]
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[PublicDashboardInfo](#PUBLICDASHBOARDINFO)
* **public_dashboard_id** (string)  `Required` 

* **name** (string)  `Required` 

* **default_layout_id** (string)  `Required` 

* **custom_layouts** (ListValue)  `Required` 

* **default_filter** (Struct)  `Required` 

* **period_type** (PeriodType)  `Required` 

* **period** (PublicDashboardPeriod)  `Required` 

* **tags** (Struct)  `Required` 

* **domain_id** (string)  `Required` 

* **created_at** (string)  `Required` 

* **updated_at** (string)  `Required` 



{{< highlight json >}}
{
   "public_dashboard_id": "pub-dash-80092b5ef658",
   "name": "Untitled Dashboard",
   "custom_layouts": [
       [
           {
               "options": {
                   "layout": 100.0,
                   "chart_type": "LINE",
                   "chart_img": "AWS_Data-Transfer_Cost_Trend",
                   "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_DATA_TRANSFER_COST_TREND_DESC"
               },
               "widget_id": "linegraph-lg-02",
               "name": "AWS Data-Transfer Cost Trend"
           }
       ],
       [
           {
               "widget_id": "map-lg-02",
               "name": "AWS Data-Transfer by Region",
               "options": {
                   "layout": 100.0,
                   "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_DATA_TRANSFER_BY_REGION_DESC",
                   "chart_img": "AWS_Data-Transfer_By_Region",
                   "chart_type": "MAP"
               }
           }
       ],
       [
           {
               "options": {
                   "chart_type": "STACKED_COLUMN",
                   "chart_img": "AWS_CloudFront_Cost",
                   "layout": 100.0,
                   "group_by": "project_id",
                   "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_CLOUDFRONT_COST_DESC"
               },
               "name": "AWS CloudFront Cost by Project",
               "widget_id": "stackedcol-lg-03"
           }
       ]
   ],
   "default_filter": {},
   "period_type": "AUTO",
   "tags": {},
   "domain_id": "domain-58010aa2e451",
   "created_at": "2022-07-19T05:42:01.412Z",
   "updated_at": "2022-07-19T05:42:01.412Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete

Deletes a specific PublicDashboard. You must specify the `public_dashboard_id` of the PublicDashboard to delete.



> **POST** /cost-analysis/v1/public-dashboard/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[PublicDashboardRequest](./PublicDashboard#publicdashboardrequest)

* **public_dashboard_id** (string)  `Required` 


* **domain_id** (string)  `Required` 





{{< highlight json >}}
{
   "public_dashboard_id": "pub-dash-579b38f00dcf"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get

Gets a specific PublicDashboard. Prints detailed information about the PublicDashboard, including `custom_layouts` and `period_type`.



> **POST** /cost-analysis/v1/public-dashboard/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[GetPublicDashboardRequest](./PublicDashboard#getpublicdashboardrequest)

* **public_dashboard_id** (string)  `Required` 


* **domain_id** (string)  `Required` 


* **only** (string) 





{{< highlight json >}}
{
   "public_dashboard_id": "pub-dash-579b38f00dcf"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[PublicDashboardInfo](#PUBLICDASHBOARDINFO)
* **public_dashboard_id** (string)  `Required` 

* **name** (string)  `Required` 

* **default_layout_id** (string)  `Required` 

* **custom_layouts** (ListValue)  `Required` 

* **default_filter** (Struct)  `Required` 

* **period_type** (PeriodType)  `Required` 

* **period** (PublicDashboardPeriod)  `Required` 

* **tags** (Struct)  `Required` 

* **domain_id** (string)  `Required` 

* **created_at** (string)  `Required` 

* **updated_at** (string)  `Required` 



{{< highlight json >}}
{
   "public_dashboard_id": "pub-dash-80092b5ef658",
   "name": "Untitled Dashboard",
   "custom_layouts": [
       [
           {
               "options": {
                   "layout": 100.0,
                   "chart_type": "LINE",
                   "chart_img": "AWS_Data-Transfer_Cost_Trend",
                   "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_DATA_TRANSFER_COST_TREND_DESC"
               },
               "widget_id": "linegraph-lg-02",
               "name": "AWS Data-Transfer Cost Trend"
           }
       ],
       [
           {
               "widget_id": "map-lg-02",
               "name": "AWS Data-Transfer by Region",
               "options": {
                   "layout": 100.0,
                   "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_DATA_TRANSFER_BY_REGION_DESC",
                   "chart_img": "AWS_Data-Transfer_By_Region",
                   "chart_type": "MAP"
               }
           }
       ],
       [
           {
               "options": {
                   "chart_type": "STACKED_COLUMN",
                   "chart_img": "AWS_CloudFront_Cost",
                   "layout": 100.0,
                   "group_by": "project_id",
                   "chart_desc_translation_id": "BILLING.COST_MANAGEMENT.DASHBOARD.CUSTOMIZE.ADD_WIDGET_MODAL.AWS_CLOUDFRONT_COST_DESC"
               },
               "name": "AWS CloudFront Cost by Project",
               "widget_id": "stackedcol-lg-03"
           }
       ]
   ],
   "default_filter": {},
   "period_type": "AUTO",
   "tags": {},
   "domain_id": "domain-58010aa2e451",
   "created_at": "2022-07-19T05:42:01.412Z",
   "updated_at": "2022-07-19T05:42:01.412Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Gets a list of all PublicDashboards. You can use a query to get a filtered list of PublicDashboards.



> **POST** /cost-analysis/v1/public-dashboard/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[PublicDashboardQuery](./PublicDashboard#publicdashboardquery)

* **domain_id** (string)  `Required` 


* **query** (Query) 


* **public_dashboard_id** (string) 


* **name** (string) 


* **period_type** (PeriodType) 





{{< highlight json >}}
{
   "query": {}
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[PublicDashboardsInfo](#PUBLICDASHBOARDSINFO)
* **results** (PublicDashboardInfo)  `Required` 

* **total_count** (int32)  `Required` 



{{< highlight json >}}
{
   "results": [
       {
           "public_dashboard_id": "pub-dash-579b38f00dcf",
           "name": "CDN & Traffic Cost",
           "custom_layouts": [
               [
                   {
                       "widget_id": "linegraph-lg-02",
                       "name": "AWS Data-Transfer Cost Trend",
                       "options": {
                           "chart_type": "LINE",
                           "layout": 100.0
                       }
                   }
               ],
               [
                   {
                       "name": "AWS CloudFront Cost by Project",
                       "options": {
                           "group_by": "project_id",
                           "chart_type": "STACKED_COLUMN",
                           "layout": 100.0
                       },
                       "widget_id": "stackedcol-lg-03"
                   }
               ],
               [
                   {
                       "options": {
                           "layout": 100.0,
                           "chart_type": "MAP"
                       },
                       "widget_id": "map-lg-02",
                       "name": "AWS Data-Transfer by Region"
                   }
               ]
           ],
           "default_filter": {
               "project_id": [],
               "service_account_id": [],
               "project_group_id": [],
               "provider": [
                   "google_cloud",
                   "azure",
                   "aws_china",
                   "aws"
               ]
           },
           "period_type": "AUTO",
           "tags": {},
           "domain_id": "domain-58010aa2e451",
           "created_at": "2022-04-07T02:31:28.197Z",
           "updated_at": "2022-04-07T02:31:28.197Z"
       },
       {
           "public_dashboard_id": "pub-dash-fc83ed9bc825",
           "name": "Monthly Cost Summary",
           "custom_layouts": [
               [
                   {
                       "options": {
                           "layout": 33.0,
                           "chart_type": "CARD"
                       },
                       "widget_id": "card-sm-01",
                       "name": "Month-to-Date Spend"
                   },
                   {
                       "name": "Last Month Total Spend",
                       "widget_id": "card-sm-02",
                       "options": {
                           "layout": 33.0,
                           "chart_type": "CARD"
                       }
                   },
                   {
                       "widget_id": "card-sm-03",
                       "name": "Budget Usage",
                       "options": {
                           "chart_type": "CARD",
                           "layout": 33.0
                       }
                   }
               ],
               [
                   {
                       "name": "Cost By Project",
                       "widget_id": "treemap-lg-01",
                       "options": {
                           "group_by": "project_id",
                           "layout": 100.0,
                           "chart_type": "TREEMAP"
                       }
                   }
               ],
               [
                   {
                       "name": "Cost Trend By Project",
                       "widget_id": "linegraph-lg-01",
                       "options": {
                           "layout": 100.0,
                           "group_by": "provider",
                           "chart_type": "LINE"
                       }
                   }
               ],
               [
                   {
                       "options": {
                           "layout": 100.0,
                           "chart_type": "STACKED_COLUMN",
                           "group_by": "product"
                       },
                       "widget_id": "stackedcol-lg-01",
                       "name": "Cost Trend By Product"
                   }
               ],
               [
                   {
                       "name": "Cost By Provider",
                       "options": {
                           "layout": 50.0,
                           "group_by": "provider",
                           "chart_type": "STACKED_COLUMN"
                       },
                       "widget_id": "donut-md-01"
                   },
                   {
                       "widget_id": "waffle-md-01",
                       "name": "Budget Status",
                       "options": {
                           "layout": 50.0,
                           "chart_type": "WAFFLE"
                       }
                   }
               ],
               [
                   {
                       "options": {
                           "chart_type": "MAP",
                           "layout": 100.0
                       },
                       "widget_id": "map-lg-01",
                       "name": "Cost By Region"
                   }
               ]
           ],
           "default_filter": {
               "provider": []
           },
           "period_type": "AUTO",
           "tags": {},
           "domain_id": "domain-58010aa2e451",
           "created_at": "2022-03-29T05:22:41.283Z",
           "updated_at": "2022-03-29T05:22:41.283Z"
       }
   ],
   "total_count": 3
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /cost-analysis/v1/public-dashboard/stat
>






    


<br>
<br>

## Message



### CreatePublicDashboardRequest
* **name** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **default_layout_id** (string) 

    
* **custom_layouts** (ListValue) 

    
* **default_filter** (Struct) 

    
* **period_type** (PeriodType) 

    
* **period** (PublicDashboardPeriod) 

    
* **tags** (Struct) 

    <br>

### GetPublicDashboardRequest
* **public_dashboard_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **only** (string) 

    <br>

### PublicDashboardInfo
* **public_dashboard_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **default_layout_id** (string)  `Required` 

    
* **custom_layouts** (ListValue)  `Required` 

    
* **default_filter** (Struct)  `Required` 

    
* **period_type** (PeriodType)  `Required` 

    
* **period** (PublicDashboardPeriod)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **updated_at** (string)  `Required` 

    <br>

### PublicDashboardPeriod
* **start** (string)  `Required` 

    
* **end** (string)  `Required` 

    <br>

### PublicDashboardQuery
* **domain_id** (string)  `Required` 

    
* **query** (Query) 

    
* **public_dashboard_id** (string) 

    
* **name** (string) 

    
* **period_type** (PeriodType) 

    <br>

### PublicDashboardRequest
* **public_dashboard_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### PublicDashboardStatQuery
* **query** (StatisticsQuery)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### PublicDashboardsInfo
* **results** (PublicDashboardInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### UpdatePublicDashboardRequest
* **public_dashboard_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **name** (string) 

    
* **default_layout_id** (string) 

    
* **custom_layouts** (ListValue) 

    
* **default_filter** (Struct) 

    
* **period_type** (PeriodType) 

    
* **period** (PublicDashboardPeriod) 

    
* **tags** (Struct) 

    <br>
