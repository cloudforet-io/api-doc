---
title: "Custom_widget"
linkTitle: "Custom_widget"
weight: 3
bookFlatSection: true
---
# [Custom_widget](#Custom_widget)
desc: A CustomWidget is a widget created by a CostQuerySet a User defined.


>  **Package : spaceone.api.cost_analysis.v1**

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

> **POST** /cost-analysis/v1/custom-widget/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /cost-analysis/v1/custom-widget/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /cost-analysis/v1/custom-widget/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /cost-analysis/v1/custom-widget/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /cost-analysis/v1/custom-widget/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /cost-analysis/v1/custom-widget/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### CreateCustomWidgetRequest
* **name** (string)  `Required` 

  *is_required: true*

    
* **options** (Struct)  `Required` 

  *is_required: true*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### CustomWidgetInfo
* **widget_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **options** (Struct)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **user_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **updated_at** (string)  `Required` 

    <br>

### CustomWidgetQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **widget_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **user_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### CustomWidgetRequest
* **widget_id** (string)  `Required` 

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
* **widget_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### UpdateCustomWidgetRequest
* **widget_id** (string)  `Required` 

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **options** (Struct)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
