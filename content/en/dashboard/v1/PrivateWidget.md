---
title: "PrivateWidget"
linkTitle: "PrivateWidget"
weight: 3
bookFlatSection: true
---
# [PrivateWidget](#PrivateWidget)
description of widget


>  **Package : spaceone.api.dashboard.v1**

<br>
<br>

## PrivateWidget





**PrivateWidget Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./PrivateWidget#create) | [CreatePrivateWidgetRequest](PrivateWidget#createprivatewidgetrequest) | [PrivateWidgetInfo](PrivateWidget#privatewidgetinfo) |
| [**update**](./PrivateWidget#update) | [UpdatePrivateWidgetRequest](PrivateWidget#updateprivatewidgetrequest) | [PrivateWidgetInfo](PrivateWidget#privatewidgetinfo) |
| [**delete**](./PrivateWidget#delete) | [PrivateWidgetRequest](PrivateWidget#privatewidgetrequest) | [Empty](PrivateWidget#empty) |
| [**load**](./PrivateWidget#load) | [LoadPrivateWidgetRequest](PrivateWidget#loadprivatewidgetrequest) | [Struct](PrivateWidget#struct) |
| [**load_sum**](./PrivateWidget#load_sum) | [LoadSumPrivateWidgetRequest](PrivateWidget#loadsumprivatewidgetrequest) | [Struct](PrivateWidget#struct) |
| [**get**](./PrivateWidget#get) | [PrivateWidgetRequest](PrivateWidget#privatewidgetrequest) | [PrivateWidgetInfo](PrivateWidget#privatewidgetinfo) |
| [**list**](./PrivateWidget#list) | [PrivateWidgetQuery](PrivateWidget#privatewidgetquery) | [PrivateWidgetsInfo](PrivateWidget#privatewidgetsinfo) |



    
<br>

### create





> **POST** /dashboard/v1/private-widget/create
>






    
<br>

### update





> **POST** /dashboard/v1/private-widget/update
>






    
<br>

### delete





> **POST** /dashboard/v1/private-widget/delete
>






    
<br>

### load





> **POST** /dashboard/v1/private-widget/load
>






    
<br>

### load_sum





> **POST** /dashboard/v1/private-widget/load-sum
>






    
<br>

### get





> **POST** /dashboard/v1/private-widget/get
>






    
<br>

### list





> **POST** /dashboard/v1/private-widget/list
>






    


<br>
<br>

## Message



### CreatePrivateWidgetRequest
* **dashboard_id** (string)   `Required` 

    
* **name** (string)  

    
* **state** (State)  

    
* **description** (string)  

    
* **widget_type** (string)  

    
* **size** (string)  

    
* **options** (Struct)  

    
* **data_table_id** (int32)  

    
* **data_tables** (Struct)  `Repeated`   

    
* **tags** (Struct)  

    <br>

### LoadPrivateWidgetRequest
* **widget_id** (string)   `Required` 

    
* **granularity** (string)   `Required` 

    
* **start** (string)   `Required` 

    
* **end** (string)   `Required` 

    
* **group_by** (string)  `Repeated`   

    
* **sort** (PrivateWidgetSort)  `Repeated`   

    
* **page** (PrivateWidgetPage)  

    
* **vars** (Struct)  

    <br>

### LoadSumPrivateWidgetRequest
* **widget_id** (string)   `Required` 

    
* **granularity** (string)   `Required` 

    
* **start** (string)   `Required` 

    
* **end** (string)   `Required` 

    
* **vars** (Struct)  

    <br>

### PrivateWidgetInfo
* **widget_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **state** (State)   `Required` 

    
* **description** (string)   `Required` 

    
* **widget_type** (string)   `Required` 

    
* **size** (string)   `Required` 

    
* **options** (Struct)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **user_id** (string)   `Required` 

    
* **dashboard_id** (string)   `Required` 

    
* **data_table_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### PrivateWidgetPage
* **start** (int32)   `Required` 

    
* **limit** (int32)   `Required` 

    <br>

### PrivateWidgetQuery
* **dashboard_id** (string)   `Required` 

    
* **query** (Query)  

    
* **widget_id** (string)  

    
* **name** (string)  

    <br>

### PrivateWidgetRequest
* **widget_id** (string)   `Required` 

    <br>

### PrivateWidgetSort
* **key** (string)   `Required` 

    
* **desc** (bool)   `Required` 

    <br>

### PrivateWidgetsInfo
* **results** (PrivateWidgetInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdatePrivateWidgetRequest
* **widget_id** (string)   `Required` 

    
* **name** (string)  

    
* **state** (State)  

    
* **description** (string)  

    
* **widget_type** (string)  

    
* **size** (string)  

    
* **options** (Struct)  

    
* **data_table_id** (string)  

    
* **tags** (Struct)  

    <br>
