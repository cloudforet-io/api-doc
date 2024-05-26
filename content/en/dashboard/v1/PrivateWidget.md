---
title: "PrivateWidget"
linkTitle: "PrivateWidget"
weight: 3
bookFlatSection: true
---
# [PrivateWidget](#PrivateWidget)
description of widget


>  **Package : spaceone.api.widget.v1**

<br>
<br>

## PrivateWidget





**PrivateWidget Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./PrivateWidget#create) | [CreatePrivateWidgetRequest](PrivateWidget#createprivatewidgetrequest) | [PrivateWidgetInfo](PrivateWidget#privatewidgetinfo) |
| [**update**](./PrivateWidget#update) | [UpdatePrivateWidgetRequest](PrivateWidget#updateprivatewidgetrequest) | [PrivateWidgetInfo](PrivateWidget#privatewidgetinfo) |
| [**delete**](./PrivateWidget#delete) | [PrivateWidgetRequest](PrivateWidget#privatewidgetrequest) | [Empty](PrivateWidget#empty) |
| [**load**](./PrivateWidget#load) | [LoadPrivateWidgetRequest](PrivateWidget#loadprivatewidgetrequest) | [PrivateWidgetInfo](PrivateWidget#privatewidgetinfo) |
| [**get**](./PrivateWidget#get) | [PrivateWidgetRequest](PrivateWidget#privatewidgetrequest) | [PrivateWidgetInfo](PrivateWidget#privatewidgetinfo) |
| [**list**](./PrivateWidget#list) | [PrivateWidgetQuery](PrivateWidget#privatewidgetquery) | [PrivateWidgetsInfo](PrivateWidget#privatewidgetsinfo) |



    
<br>

### create





> **POST** /widget/v1/private-widget/create
>






    
<br>

### update





> **POST** /widget/v1/private-widget/update
>






    
<br>

### delete





> **POST** /widget/v1/private-widget/delete
>






    
<br>

### load





> **POST** /widget/v1/private-widget/load
>






    
<br>

### get





> **POST** /widget/v1/private-widget/get
>






    
<br>

### list





> **POST** /widget/v1/private-widget/list
>






    


<br>
<br>

## Message



### CreatePrivateWidgetRequest
* **private_dashboard_id** (string)   `Required` 

    
* **name** (string)  

    
* **description** (string)  

    
* **widget_type** (string)  

    
* **options** (Struct)  

    
* **tags** (Struct)  

    <br>

### LoadPrivateWidgetRequest
* **widget_id** (string)   `Required` 

    
* **sort** (Sort)  `Repeated`   

    
* **page** (Page)  

    
* **vars** (Struct)  

    <br>

### PrivateWidgetInfo
* **widget_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **description** (string)   `Required` 

    
* **widget_type** (string)   `Required` 

    
* **options** (Struct)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **user_id** (string)   `Required` 

    
* **private_dashboard_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### PrivateWidgetQuery
* **private_dashboard_id** (string)   `Required` 

    
* **query** (Query)  

    
* **widget_id** (string)  

    
* **name** (string)  

    <br>

### PrivateWidgetRequest
* **widget_id** (string)   `Required` 

    <br>

### PrivateWidgetsInfo
* **results** (PrivateWidgetInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdatePrivateWidgetRequest
* **widget_id** (string)   `Required` 

    
* **name** (string)  

    
* **description** (string)  

    
* **widget_type** (string)  

    
* **options** (Struct)  

    
* **tags** (Struct)  

    <br>
