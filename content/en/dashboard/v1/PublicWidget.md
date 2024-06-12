---
title: "PublicWidget"
linkTitle: "PublicWidget"
weight: 3
bookFlatSection: true
---
# [PublicWidget](#PublicWidget)
description of widget


>  **Package : spaceone.api.dashboard.v1**

<br>
<br>

## PublicWidget





**PublicWidget Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./PublicWidget#create) | [CreatePublicWidgetRequest](PublicWidget#createpublicwidgetrequest) | [PublicWidgetInfo](PublicWidget#publicwidgetinfo) |
| [**update**](./PublicWidget#update) | [UpdatePublicWidgetRequest](PublicWidget#updatepublicwidgetrequest) | [PublicWidgetInfo](PublicWidget#publicwidgetinfo) |
| [**delete**](./PublicWidget#delete) | [PublicWidgetRequest](PublicWidget#publicwidgetrequest) | [Empty](PublicWidget#empty) |
| [**load**](./PublicWidget#load) | [LoadPublicWidgetRequest](PublicWidget#loadpublicwidgetrequest) | [Struct](PublicWidget#struct) |
| [**get**](./PublicWidget#get) | [PublicWidgetRequest](PublicWidget#publicwidgetrequest) | [PublicWidgetInfo](PublicWidget#publicwidgetinfo) |
| [**list**](./PublicWidget#list) | [PublicWidgetQuery](PublicWidget#publicwidgetquery) | [PublicWidgetsInfo](PublicWidget#publicwidgetsinfo) |



    
<br>

### create





> **POST** /dashboard/v1/public-widget/create
>






    
<br>

### update





> **POST** /dashboard/v1/public-widget/update
>






    
<br>

### delete





> **POST** /dashboard/v1/public-widget/delete
>






    
<br>

### load





> **POST** /dashboard/v1/public-widget/load
>






    
<br>

### get





> **POST** /dashboard/v1/public-widget/get
>






    
<br>

### list





> **POST** /dashboard/v1/public-widget/list
>






    


<br>
<br>

## Message



### CreatePublicWidgetRequest
* **dashboard_id** (string)   `Required` 

    
* **name** (string)  

    
* **description** (string)  

    
* **widget_type** (string)  

    
* **size** (string)  

    
* **options** (Struct)  

    
* **tags** (Struct)  

    <br>

### LoadPublicWidgetRequest
* **widget_id** (string)   `Required` 

    
* **query** (TimeSeriesAnalyzeQuery)   `Required` 

    
* **vars** (Struct)  

    <br>

### PublicWidgetInfo
* **widget_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **description** (string)   `Required` 

    
* **widget_type** (string)   `Required` 

    
* **size** (string)   `Required` 

    
* **options** (Struct)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **resource_group** (ResourceGroup)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **workspace_id** (string)   `Required` 

    
* **project_id** (string)   `Required` 

    
* **dashboard_id** (string)   `Required` 

    
* **data_table_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    
* **updated_at** (string)   `Required` 

    <br>

### PublicWidgetQuery
* **dashboard_id** (string)   `Required` 

    
* **query** (Query)  

    
* **widget_id** (string)  

    
* **name** (string)  

    <br>

### PublicWidgetRequest
* **widget_id** (string)   `Required` 

    <br>

### PublicWidgetsInfo
* **results** (PublicWidgetInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### UpdatePublicWidgetRequest
* **widget_id** (string)   `Required` 

    
* **name** (string)  

    
* **description** (string)  

    
* **widget_type** (string)  

    
* **size** (string)  

    
* **options** (Struct)  

    
* **data_table_id** (string)  

    
* **tags** (Struct)  

    <br>
