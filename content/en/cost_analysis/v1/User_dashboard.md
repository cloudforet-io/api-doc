---
title: "User_dashboard"
linkTitle: "User_dashboard"
weight: 3
bookFlatSection: true
---
# [User_dashboard](#User_dashboard)
desc: A UserDashboard is a cost data dashboard customized with a combination of widgets a User want.


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

> **POST** /cost-analysis/v1/user-dashboard/create
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /cost-analysis/v1/user-dashboard/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### delete

> **POST** /cost-analysis/v1/user-dashboard/delete
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /cost-analysis/v1/user-dashboard/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /cost-analysis/v1/user-dashboard/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /cost-analysis/v1/user-dashboard/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### CreateUserDashboardRequest
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

    
* **period** (UserDashboardPeriod)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### GetUserDashboardRequest
* **user_dashboard_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### UpdateUserDashboardRequest
* **user_dashboard_id** (string)  `Required` 

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

    
* **period** (UserDashboardPeriod)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

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
* **query** (Query)  `Required` 

  *is_required: false*

    
* **user_dashboard_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **period_type** (PeriodType)  `Required` 

  *is_required: false*

    
* **user_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### UserDashboardRequest
* **user_dashboard_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### UserDashboardStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### UserDashboardsInfo
* **results** (UserDashboardInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>
