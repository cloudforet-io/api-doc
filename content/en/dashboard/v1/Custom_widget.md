---
title: "Custom_widget"
linkTitle: "Custom_widget"
weight: 3
bookFlatSection: true
---
# [Custom_widget](#Custom_widget)
desc: description of dashboard


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




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /dashboard/v1/custom-widget/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /dashboard/v1/custom-widget/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /dashboard/v1/custom-widget/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /dashboard/v1/custom-widget/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /dashboard/v1/custom-widget/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### CreateCustomWidgetRequest
* **widget_name** (string)  `Required` 

  *is_required: true*

    
* **title** (string)  `Required` 

  *is_required: true*

    
* **options** (Struct)  `Required` 

  *is_required: true*

    
* **settings** (Struct)  `Required` 

  *is_required: false*

    
* **inherit_options** (Struct)  `Required` 

  *is_required: false*

    
* **labels** (ListValue)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

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
* **query** (Query)  `Required` 

  *is_required: false*

    
* **custom_widget_id** (string)  `Required` 

  *is_required: false*

    
* **widget_name** (string)  `Required` 

  *is_required: false*

    
* **title** (string)  `Required` 

  *is_required: false*

    
* **user_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### CustomWidgetRequest
* **custom_widget_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### CustomWidgetStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### CustomWidgetsInfo
* **results** (CustomWidgetInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### GetCustomWidgetRequest
* **custom_widget_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### UpdateCustomWidgetRequest
* **custom_widget_id** (string)  `Required` 

  *is_required: true*

    
* **title** (string)  `Required` 

  *is_required: false*

    
* **options** (Struct)  `Required` 

  *is_required: false*

    
* **settings** (Struct)  `Required` 

  *is_required: false*

    
* **inherit_options** (Struct)  `Required` 

  *is_required: false*

    
* **labels** (ListValue)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
