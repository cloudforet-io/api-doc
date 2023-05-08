---
title: "Public_dashboard"
linkTitle: "Public_dashboard"
weight: 3
bookFlatSection: true
---
# [Public_dashboard](#Public_dashboard)
desc: A PublicDashboard is a cost data dashboard provided to all users by default.


>  **Package : spaceone.api.cost_analysis.v1**

<br>
<br>

## Public_dashboard


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

> **POST** /cost-analysis/v1/public-dashboard/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /cost-analysis/v1/public-dashboard/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /cost-analysis/v1/public-dashboard/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /cost-analysis/v1/public-dashboard/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /cost-analysis/v1/public-dashboard/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /cost-analysis/v1/public-dashboard/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### CreatePublicDashboardRequest
* **name** (string)  `Required` 

  *is_required: true*

    
* **default_layout_id** (string)  `Required` 

  *is_required: false*

    
* **custom_layouts** (ListValue)  `Required` 

  *is_required: false*

    
* **default_filter** (Struct)  `Required` 

  *is_required: false*

    
* **period_type** (PeriodType)  `Required` 

  *is_required: false*

    
* **period** (PublicDashboardPeriod)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### GetPublicDashboardRequest
* **public_dashboard_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

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
* **query** (Query)  `Required` 

  *is_required: false*

    
* **public_dashboard_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **period_type** (PeriodType)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### PublicDashboardRequest
* **public_dashboard_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### PublicDashboardStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### PublicDashboardsInfo
* **results** (PublicDashboardInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### UpdatePublicDashboardRequest
* **public_dashboard_id** (string)  `Required` 

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **default_layout_id** (string)  `Required` 

  *is_required: false*

    
* **custom_layouts** (ListValue)  `Required` 

  *is_required: false*

    
* **default_filter** (Struct)  `Required` 

  *is_required: false*

    
* **period_type** (PeriodType)  `Required` 

  *is_required: false*

    
* **period** (PublicDashboardPeriod)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
