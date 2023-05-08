---
title: "Data_source"
linkTitle: "Data_source"
weight: 3
bookFlatSection: true
---
# [Data_source](#Data_source)
desc: A DataSource is a plugin instance collecting `metric` and `log` data from Cloudforet.


>  **Package : spaceone.api.monitoring.v1**

<br>
<br>

## Data_source


**DataSource Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**register**](./DataSource#register) | [RegisterDataSourceRequest](DataSource#registerdatasourcerequest) | [DataSourceInfo](./DataSource#datasourceinfo) |
| [**update**](./DataSource#update) | [UpdateDataSourceRequest](DataSource#updatedatasourcerequest) | [DataSourceInfo](./DataSource#datasourceinfo) |
| [**enable**](./DataSource#enable) | [DataSourceRequest](DataSource#datasourcerequest) | [DataSourceInfo](./DataSource#datasourceinfo) |
| [**disable**](./DataSource#disable) | [DataSourceRequest](DataSource#datasourcerequest) | [DataSourceInfo](./DataSource#datasourceinfo) |
| [**deregister**](./DataSource#deregister) | [DataSourceRequest](DataSource#datasourcerequest) | [Empty](./DataSource#empty) |
| [**update_plugin**](./DataSource#update_plugin) | [UpdateDataSourcePluginRequest](DataSource#updatedatasourcepluginrequest) | [DataSourceInfo](./DataSource#datasourceinfo) |
| [**verify_plugin**](./DataSource#verify_plugin) | [DataSourceRequest](DataSource#datasourcerequest) | [Empty](./DataSource#empty) |
| [**get**](./DataSource#get) | [GetDataSourceRequest](DataSource#getdatasourcerequest) | [DataSourceInfo](./DataSource#datasourceinfo) |
| [**list**](./DataSource#list) | [DataSourceQuery](DataSource#datasourcequery) | [DataSourcesInfo](./DataSource#datasourcesinfo) |
| [**stat**](./DataSource#stat) | [DataSourceStatQuery](DataSource#datasourcestatquery) | [Struct](./DataSource#struct) |



    
<br>

### register

> **POST** /monitoring/v1/data-source/register
>




 {{< tabs " register " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /monitoring/v1/data-source/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### enable

> **POST** /monitoring/v1/data-source/enable
>




 {{< tabs " enable " >}}




{{< /tabs >}}

    
<br>

### disable

> **POST** /monitoring/v1/data-source/disable
>




 {{< tabs " disable " >}}




{{< /tabs >}}

    
<br>

### deregister

> **POST** /monitoring/v1/data-source/deregister
>




 {{< tabs " deregister " >}}




{{< /tabs >}}

    
<br>

### update_plugin

> **POST** /monitoring/v1/data-source/update-plugin
>




 {{< tabs " update_plugin " >}}




{{< /tabs >}}

    
<br>

### verify_plugin

> **POST** /monitoring/v1/data-source/verify-plugin
>




 {{< tabs " verify_plugin " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /monitoring/v1/data-source/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /monitoring/v1/data-source/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /monitoring/v1/data-source/stat
>




 {{< tabs " stat " >}}




{{< /tabs >}}

    


<br>
<br>

## Message



### DataSourceInfo
* **data_source_id** (string)  `Required` 

    
* **name** (string)  `Required` 

    
* **state** (State)  `Required` 

    
* **monitoring_type** (MonitoringType)  `Required` 

    
* **provider** (string)  `Required` 

    
* **capability** (Struct)  `Required` 

    
* **plugin_info** (DataSourcePluginInfo)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    <br>

### DataSourcePluginInfo
* **plugin_id** (string)  `Required` 

    
* **version** (string)  `Required` 

    
* **options** (Struct)  `Required` 

    
* **metadata** (Struct)  `Required` 

    
* **upgrade_mode** (UpgradeMode)  `Required` 

    
* **secret_id** (string)  `Required` 

    
* **provider** (string)  `Required` 

    <br>

### DataSourceQuery
* **query** (Query)  `Required` 

  *is_required: false*

    
* **data_source_id** (string)  `Required` 

  *is_required: false*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **state** (string)  `Required` 

  *is_required: false*

    
* **monitoring_type** (MonitoringType)  `Required` 

  *is_required: false*

    
* **provider** (string)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### DataSourceRequest
* **data_source_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### DataSourceStatQuery
* **query** (StatisticsQuery)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### DataSourcesInfo
* **results** (DataSourceInfo)  `Required` 

    
* **total_count** (int32)  `Required` 

    <br>

### GetDataSourceRequest
* **data_source_id** (string)  `Required` 

  *is_required: true*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    
* **only** (string)  `Required` 

  *is_required: false*

    <br>

### RegisterDataSourceRequest
* **name** (string)  `Required` 

  *is_required: true*

    
* **plugin_info** (DataSourcePluginInfo)  `Required` 

  *is_required: true*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### UpdateDataSourcePluginRequest
* **data_source_id** (string)  `Required` 

  *is_required: true*

    
* **version** (string)  `Required` 

  *is_required: false*

    
* **options** (Struct)  `Required` 

  *is_required: false*

    
* **upgrade_mode** (UpgradeMode)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### UpdateDataSourceRequest
* **data_source_id** (string)  `Required` 

  *is_required: true*

    
* **name** (string)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
