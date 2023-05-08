---
title: "Domain_dashboard"
linkTitle: "Domain_dashboard"
weight: 3
bookFlatSection: true
---
# [Domain_dashboard](#Domain_dashboard)
desc: description of dashboard


>  **Package : spaceone.api.dashboard.v1**

<br>
<br>

## Domain_dashboard


**DomainDashboard Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**create**](./DomainDashboard#create) | [CreateDomainDashboardRequest](DomainDashboard#createdomaindashboardrequest) | [DomainDashboardInfo](./DomainDashboard#domaindashboardinfo) |
| [**update**](./DomainDashboard#update) | [UpdateDomainDashboardRequest](DomainDashboard#updatedomaindashboardrequest) | [DomainDashboardInfo](./DomainDashboard#domaindashboardinfo) |
| [**delete**](./DomainDashboard#delete) | [DomainDashboardRequest](DomainDashboard#domaindashboardrequest) | [Empty](./DomainDashboard#empty) |
| [**get**](./DomainDashboard#get) | [GetDomainDashboardRequest](DomainDashboard#getdomaindashboardrequest) | [DomainDashboardInfo](./DomainDashboard#domaindashboardinfo) |
| [**delete_version**](./DomainDashboard#delete_version) | [DomainDashboardVersionRequest](DomainDashboard#domaindashboardversionrequest) | [Empty](./DomainDashboard#empty) |
| [**revert_version**](./DomainDashboard#revert_version) | [DomainDashboardVersionRequest](DomainDashboard#domaindashboardversionrequest) | [DomainDashboardInfo](./DomainDashboard#domaindashboardinfo) |
| [**get_version**](./DomainDashboard#get_version) | [GetDomainDashboardVersionRequest](DomainDashboard#getdomaindashboardversionrequest) | [DomainDashboardVersionInfo](./DomainDashboard#domaindashboardversioninfo) |
| [**list_versions**](./DomainDashboard#list_versions) | [DomainDashboardVersionQuery](DomainDashboard#domaindashboardversionquery) | [DomainDashboardVersionsInfo](./DomainDashboard#domaindashboardversionsinfo) |
| [**list**](./DomainDashboard#list) | [DomainDashboardQuery](DomainDashboard#domaindashboardquery) | [DomainDashboardsInfo](./DomainDashboard#domaindashboardsinfo) |
| [**stat**](./DomainDashboard#stat) | [DomainDashboardStatQuery](DomainDashboard#domaindashboardstatquery) | [Struct](./DomainDashboard#struct) |



    
<br>

### create

> **POST** /dashboard/v1/domain-dashboards
>




 {{< tabs " create " >}}




{{< /tabs >}}

    
<br>

### update

> **PUT** /dashboard/v1/domain-dashboard/{domain_dashboard_id}
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### delete

> **DELETE** /dashboard/v1/domain-dashboard/{domain_dashboard_id}
>




 {{< tabs " delete " >}}




{{< /tabs >}}

    
<br>

### get

> **GET** /dashboard/v1/domain-dashboard/{domain_dashboard_id}
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### delete_version

> **DELETE** /dashboard/v1/domain-dashboard/{domain_dashboard_id}/version/{version}
>




 {{< tabs " delete_version " >}}




{{< /tabs >}}

    
<br>

### revert_version

> **POST** /dashboard/v1/domain-dashboard/{domain_dashboard_id}/version/{version}/revert
>




 {{< tabs " revert_version " >}}




{{< /tabs >}}

    
<br>

### get_version

> **GET** /dashboard/v1/domain-dashboard/{domain_dashboard_id}/version/{version}
>




 {{< tabs " get_version " >}}




{{< /tabs >}}

    
<br>

### list_versions

> **GET** /dashboard/v1/domain-dashboard/{domain_dashboard_id}/versions
>




 {{< tabs " list_versions " >}}




{{< /tabs >}}

    
<br>

### list

> **GET** /dashboard/v1/domain-dashboards
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /dashboard/v1/domain-dashboards/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### CreateDomainDashboardRequest
* **name** (string)  `Required` 

  *is_required: true*

    
* **viewers** (Viewers)  `Required` 

  *is_required: true*

    
* **layouts** (ListValue)  `Required` 

  *is_required: false*

    
* **variables** (Struct)  `Required` 

  *is_required: false*

    
* **settings** (Struct)  `Required` 

  *is_required: false*

    
* **variables_schema** (Struct)  `Required` 

  *is_required: false*

    
* **labels** (ListValue)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### DomainDashboardInfo
* **domain_dashboard_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **viewers** (Viewers)  `Required` 

    
* **version** (int32)  `Required` 

    
* **layouts** (ListValue)  `Required` 

    
* **variables** (Struct)  `Required` 

    
* **settings** (Struct)  `Required` 

    
* **variables_schema** (Struct)  `Required` 

    
* **labels** (ListValue)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **user_id** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **updated_at** (string)  `Required` 

    <br>

### DomainDashboardQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **domain_dashboard_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **viewers** (Viewers)  `Required` 

  *is_required: false*

    
* **user_id** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### DomainDashboardRequest
* **domain_dashboard_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### DomainDashboardStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### DomainDashboardVersionInfo
* **domain_dashboard_id** (string)  `Required` 

    
* **version** (int32)  `Required` 

    
* **latest** (bool)  `Required` 

    
* **layouts** (ListValue)  `Required` 

    
* **variables** (Struct)  `Required` 

    
* **settings** (Struct)  `Required` 

    
* **variables_schema** (Struct)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    <br>

### DomainDashboardVersionQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **domain_dashboard_id** (string)  `Required` 

  *is_required: true*

    
* **version** (int32)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### DomainDashboardVersionRequest
* **domain_dashboard_id** (string)  `Required` 

  *is_required: true*

    
* **version** (int32)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### DomainDashboardVersionsInfo
* **results** (DomainDashboardVersionInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### DomainDashboardsInfo
* **results** (DomainDashboardInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### GetDomainDashboardRequest
* **domain_dashboard_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### GetDomainDashboardVersionRequest
* **domain_dashboard_id** (string)  `Required` 

  *is_required: true*

    
* **version** (int32)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### UpdateDomainDashboardRequest
* **domain_dashboard_id** (string)  `Required` 

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **layouts** (ListValue)  `Required` 

  *is_required: false*

    
* **variables** (Struct)  `Required` 

  *is_required: false*

    
* **settings** (Struct)  `Required` 

  *is_required: false*

    
* **variables_schema** (Struct)  `Required` 

  *is_required: false*

    
* **labels** (ListValue)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
