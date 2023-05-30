---
title: "CustomWidget"
linkTitle: "CustomWidget"
weight: 3
bookFlatSection: true
---
# [CustomWidget](#CustomWidget)
A CustomWidget is a widget created by a CostQuerySet a User defined.


>  **Package : spaceone.api.cost_analysis.v1**

<br>
<br>

## CustomWidget





**CustomWidget Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./CustomWidget#create) | [CreateCustomWidgetRequest](CustomWidget#createcustomwidgetrequest) | [CustomWidgetInfo](CustomWidget#customwidgetinfo) |
| [**update**](./CustomWidget#update) | [UpdateCustomWidgetRequest](CustomWidget#updatecustomwidgetrequest) | [CustomWidgetInfo](CustomWidget#customwidgetinfo) |
| [**delete**](./CustomWidget#delete) | [CustomWidgetRequest](CustomWidget#customwidgetrequest) | [Empty](CustomWidget#empty) |
| [**get**](./CustomWidget#get) | [GetCustomWidgetRequest](CustomWidget#getcustomwidgetrequest) | [CustomWidgetInfo](CustomWidget#customwidgetinfo) |
| [**list**](./CustomWidget#list) | [CustomWidgetQuery](CustomWidget#customwidgetquery) | [CustomWidgetsInfo](CustomWidget#customwidgetsinfo) |
| [**stat**](./CustomWidget#stat) | [CustomWidgetStatQuery](CustomWidget#customwidgetstatquery) | [Struct](CustomWidget#struct) |



    
<br>

### create

Creates a new CustomWidget. Based on the queries of the CostQuerySet the User made, a widget is created with the default template Cloudforet provides.



> **POST** /cost-analysis/v1/custom-widget/create
>





 {{< tabs " create " >}}

 {{< tab "Request Example" >}}



[CreateCustomWidgetRequest](./CustomWidget#createcustomwidgetrequest)

* **name** (string)   `Required` 


* **options** (Struct)   `Required` 


* **domain_id** (string)   `Required` 


* **tags** (Struct)  





{{< highlight json >}}
{
   "name": "project_provider_region-f59722cf-dc03-4758-ab7f",
   "options": {
       "group_by": "project_id",
       "stack": false,
       "layout": 100.0,
       "granularity": "ACCUMULATED",
       "filters": {},
       "chart_type": "DONUT"
   }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CustomWidgetInfo](#CUSTOMWIDGETINFO)
* **widget_id** (string)   `Required` 

* **name** (string)   `Required` 

* **options** (Struct)   `Required` 

* **tags** (Struct)   `Required` 

* **user_id** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{
   "widget_id": "widget-8b1241aff67d",
   "name": "project_provider_region-f59722cf-dc03-4758-ab7f",
   "options": {
       "filters": {},
       "group_by": "project_id",
       "granularity": "ACCUMULATED",
       "layout": 100.0,
       "stack": false,
       "chart_type": "DONUT"
   },
   "tags": {},
   "user_id": "test_user@cloudforet.io",
   "domain_id": "domain-58010aa2e451",
   "created_at": "2022-07-19T06:18:55.819Z",
   "updated_at": "2022-07-19T06:18:55.819Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update

Updates a specific CustomWidget. You can make changes in CustomWidget settings, including `chart_type` and queries.



> **POST** /cost-analysis/v1/custom-widget/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateCustomWidgetRequest](./CustomWidget#updatecustomwidgetrequest)

* **widget_id** (string)   `Required` 


* **domain_id** (string)   `Required` 


* **name** (string)  


* **options** (Struct)  


* **tags** (Struct)  





{{< highlight json >}}
{
   "widget_id": "widget-8b1241aff67d",
   "name": "project_provider_region",
   "options": {
       "layout": 100.0,
       "chart_type": "DONUT",
       "stack": false,
       "group_by": "project_id",
       "granularity": "ACCUMULATED",
       "filters": {}
   },
   "tags": {
       "a": "b"
   }
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CustomWidgetInfo](#CUSTOMWIDGETINFO)
* **widget_id** (string)   `Required` 

* **name** (string)   `Required` 

* **options** (Struct)   `Required` 

* **tags** (Struct)   `Required` 

* **user_id** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{
   "widget_id": "widget-8b1241aff67d",
   "name": "project_provider_region-f59722cf-dc03-4758-ab7f",
   "options": {
       "filters": {},
       "group_by": "project_id",
       "granularity": "ACCUMULATED",
       "layout": 100.0,
       "stack": false,
       "chart_type": "DONUT"
   },
   "tags": {},
   "user_id": "test_user@cloudforet.io",
   "domain_id": "domain-58010aa2e451",
   "created_at": "2022-07-19T06:18:55.819Z",
   "updated_at": "2022-07-19T06:18:55.819Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### delete

Deletes a specific CustomWidget. You must specify the `custom_widget_id` of the CustomWidget to delete.



> **POST** /cost-analysis/v1/custom-widget/delete
>





 {{< tabs " delete " >}}

 {{< tab "Request Example" >}}



[CustomWidgetRequest](./CustomWidget#customwidgetrequest)

* **widget_id** (string)   `Required` 


* **domain_id** (string)   `Required` 





{{< highlight json >}}
{
   "widget_id": "widget-205f743a9890"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get

Gets a specific CustomWidget. Prints detailed information about the CustomWidget, including `chart_type` and queries.



> **POST** /cost-analysis/v1/custom-widget/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[GetCustomWidgetRequest](./CustomWidget#getcustomwidgetrequest)

* **widget_id** (string)   `Required` 


* **domain_id** (string)   `Required` 


* **only** (string)  `Repeated`   





{{< highlight json >}}
{
   "widget_id": "widget-205f743a9890"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CustomWidgetInfo](#CUSTOMWIDGETINFO)
* **widget_id** (string)   `Required` 

* **name** (string)   `Required` 

* **options** (Struct)   `Required` 

* **tags** (Struct)   `Required` 

* **user_id** (string)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 

* **updated_at** (string)   `Required` 



{{< highlight json >}}
{
   "widget_id": "widget-8b1241aff67d",
   "name": "project_provider_region-f59722cf-dc03-4758-ab7f",
   "options": {
       "filters": {},
       "group_by": "project_id",
       "granularity": "ACCUMULATED",
       "layout": 100.0,
       "stack": false,
       "chart_type": "DONUT"
   },
   "tags": {},
   "user_id": "test_user@cloudforet.io",
   "domain_id": "domain-58010aa2e451",
   "created_at": "2022-07-19T06:18:55.819Z",
   "updated_at": "2022-07-19T06:18:55.819Z"
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Gets a list of all CustomWidgets. You can use a query to get a filtered list of CustomWidgets.



> **POST** /cost-analysis/v1/custom-widget/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[CustomWidgetQuery](./CustomWidget#customwidgetquery)

* **domain_id** (string)   `Required` 


* **query** (Query)  


* **widget_id** (string)  


* **name** (string)  


* **user_id** (string)  





{{< highlight json >}}
{
   "query": {}
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[CustomWidgetsInfo](#CUSTOMWIDGETSINFO)
* **results** (CustomWidgetInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
{
   "results": [
       {
           "widget_id": "widget-205f743a9890",
           "name": "3 month product pie chart-a6752241-0a0b-4604-9186",
           "options": {
               "stack": false,
               "layout": 100.0,
               "granularity": "ACCUMULATED",
               "filters": {},
               "chart_type": "DONUT",
               "group_by": "product"
           },
           "tags": {},
           "user_id": "yuda@mz.co.kr",
           "domain_id": "domain-58010aa2e451",
           "created_at": "2022-03-08T03:37:42.967Z",
           "updated_at": "2022-03-08T03:37:42.967Z"
       },
       {
           "widget_id": "widget-c672e1501066",
           "name": "6 month project group-589318f7-ee8d-4018-9d56",
           "options": {
               "stack": false,
               "layout": 100.0,
               "chart_type": "STACKED_COLUMN",
               "filters": {},
               "group_by": "project_group_id",
               "granularity": "MONTHLY"
           },
           "tags": {},
           "user_id": "yuda@mz.co.kr",
           "domain_id": "domain-58010aa2e451",
           "created_at": "2022-03-14T09:30:03.115Z",
           "updated_at": "2022-03-14T09:30:03.115Z"
       }
   ],
   "total_count": 27
}
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /cost-analysis/v1/custom-widget/stat
>






    


<br>
<br>

## Message



### CreateCustomWidgetRequest
* **name** (string)   `Required` 

    
* **options** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **tags** (Struct)  

    <br>

### CustomWidgetInfo
* **widget_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **options** (Struct)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **user_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### CustomWidgetQuery
* **domain_id** (string)   `Required` 

    
* **query** (Query)  

    
* **widget_id** (string)  

    
* **name** (string)  

    
* **user_id** (string)  

    <br>

### CustomWidgetRequest
* **widget_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### CustomWidgetStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### CustomWidgetsInfo
* **results** (CustomWidgetInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### GetCustomWidgetRequest
* **widget_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **only** (string)  `Repeated`   

    <br>

### UpdateCustomWidgetRequest
* **widget_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **name** (string)  

    
* **options** (Struct)  

    
* **tags** (Struct)  

    <br>
