---
title: "Custom_widget"
linkTitle: "Custom_widget"
weight: 3
bookFlatSection: true
---
# [Custom_widget](#Custom_widget)
description of dashboard


>  **Package : spaceone.api.dashboard.v1**

<br>
<br>

## Custom_widget





**CustomWidget Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./CustomWidget#create) | [CreateCustomWidgetRequest](CustomWidget#createcustomwidgetrequest) | [CustomWidgetInfo](./CustomWidget#customwidgetinfo) |
| [**update**](./CustomWidget#update) | [UpdateCustomWidgetRequest](CustomWidget#updatecustomwidgetrequest) | [CustomWidgetInfo](./CustomWidget#customwidgetinfo) |
| [**delete**](./CustomWidget#delete) | [CustomWidgetRequest](CustomWidget#customwidgetrequest) | [Empty](./CustomWidget#empty) |
| [**get**](./CustomWidget#get) | [GetCustomWidgetRequest](CustomWidget#getcustomwidgetrequest) | [CustomWidgetInfo](./CustomWidget#customwidgetinfo) |
| [**list**](./CustomWidget#list) | [CustomWidgetQuery](CustomWidget#customwidgetquery) | [CustomWidgetsInfo](./CustomWidget#customwidgetsinfo) |
| [**stat**](./CustomWidget#stat) | [CustomWidgetStatQuery](CustomWidget#customwidgetstatquery) | [Struct](./CustomWidget#struct) |



    
<br>

### create





> **POST** /dashboard/v1/custom-widget/create
>






    
<br>

### update





> **POST** /dashboard/v1/custom-widget/update
>






    
<br>

### delete





> **POST** /dashboard/v1/custom-widget/delete
>






    
<br>

### get





> **POST** /dashboard/v1/custom-widget/get
>






    
<br>

### list





> **POST** /dashboard/v1/custom-widget/list
>






    
<br>

### stat





> **POST** /dashboard/v1/custom-widget/stat
>






    


<br>
<br>

## Message



### CreateCustomWidgetRequest
* **widget_name** (string)  `Required` 

    
* **title** (string)  `Required` 

    
* **options** (Struct)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **settings** (Struct) 

    
* **inherit_options** (Struct) 

    
* **labels** (ListValue) 

    
* **tags** (Struct) 

    <br>

### CustomWidgetInfo
* **custom_widget_id** (string)  `Required` 

    
* **widget_name** (string)  `Required` 

    
* **title** (string)  `Required` 

    
* **version** (string)  `Required` 

    
* **options** (Struct)  `Required` 

    
* **settings** (Struct)  `Required` 

    
* **inherit_options** (Struct)  `Required` 

    
* **labels** (ListValue)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **user_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **updated_at** (string)  `Required` 

    <br>

### CustomWidgetQuery
* **domain_id** (string)  `Required` 

    
* **query** (Query) 

    
* **custom_widget_id** (string) 

    
* **widget_name** (string) 

    
* **title** (string) 

    
* **user_id** (string) 

    <br>

### CustomWidgetRequest
* **custom_widget_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### CustomWidgetStatQuery
* **query** (StatisticsQuery)  `Required` 

    
* **domain_id** (string)  `Required` 

    <br>

### CustomWidgetsInfo
* **results** (CustomWidgetInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### GetCustomWidgetRequest
* **custom_widget_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **only** (string) 

    <br>

### UpdateCustomWidgetRequest
* **custom_widget_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **title** (string) 

    
* **options** (Struct) 

    
* **settings** (Struct) 

    
* **inherit_options** (Struct) 

    
* **labels** (ListValue) 

    
* **tags** (Struct) 

    <br>
