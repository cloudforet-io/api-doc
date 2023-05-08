---
title: "Data_source"
linkTitle: "Data_source"
weight: 3
bookFlatSection: true
---
# [Data_source](#Data_source)
desc: A DataSource is a plugin instance collecting external cost data. External cost data consists of `raw data` and the plugin information used for collection.


>  **Package : spaceone.api.cost_analysis.v1**

<br>
<br>

## Data_source


**DataSource Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**register**](./DataSource#register) | [RegisterDataSourceRequest](DataSource#registerdatasourcerequest) | [DataSourceInfo](./DataSource#datasourceinfo) |
| [**update**](./DataSource#update) | [UpdateDataSourceRequest](DataSource#updatedatasourcerequest) | [DataSourceInfo](./DataSource#datasourceinfo) |
| [**update_plugin**](./DataSource#update_plugin) | [UpdateDataSourcePluginRequest](DataSource#updatedatasourcepluginrequest) | [DataSourceInfo](./DataSource#datasourceinfo) |
| [**verify_plugin**](./DataSource#verify_plugin) | [DataSourceRequest](DataSource#datasourcerequest) | [Empty](./DataSource#empty) |
| [**enable**](./DataSource#enable) | [DataSourceRequest](DataSource#datasourcerequest) | [DataSourceInfo](./DataSource#datasourceinfo) |
| [**disable**](./DataSource#disable) | [DataSourceRequest](DataSource#datasourcerequest) | [DataSourceInfo](./DataSource#datasourceinfo) |
| [**deregister**](./DataSource#deregister) | [DataSourceRequest](DataSource#datasourcerequest) | [Empty](./DataSource#empty) |
| [**sync**](./DataSource#sync) | [SyncDataSourceRequest](DataSource#syncdatasourcerequest) | [JobInfo](./DataSource#jobinfo) |
| [**get**](./DataSource#get) | [GetDataSourceRequest](DataSource#getdatasourcerequest) | [DataSourceInfo](./DataSource#datasourceinfo) |
| [**list**](./DataSource#list) | [DataSourceQuery](DataSource#datasourcequery) | [DataSourcesInfo](./DataSource#datasourcesinfo) |
| [**stat**](./DataSource#stat) | [DataSourceStatQuery](DataSource#datasourcestatquery) | [Struct](./DataSource#struct) |



    
<br>

### register

> **POST** /cost-analysis/v1/data-source/register
>




 {{< tabs " register " >}}




{{< /tabs >}}

    
<br>

### update

> **POST** /cost-analysis/v1/data-source/update
>




 {{< tabs " update " >}}




{{< /tabs >}}

    
<br>

### update_plugin

> **POST** /cost-analysis/v1/data-source/update-plugin
>




 {{< tabs " update_plugin " >}}




{{< /tabs >}}

    
<br>

### verify_plugin

> **POST** /cost-analysis/v1/data-source/verify-plugin
>




 {{< tabs " verify_plugin " >}}




{{< /tabs >}}

    
<br>

### enable

> **POST** /cost-analysis/v1/data-source/enable
>




 {{< tabs " enable " >}}




{{< /tabs >}}

    
<br>

### disable

> **POST** /cost-analysis/v1/data-source/disable
>




 {{< tabs " disable " >}}




{{< /tabs >}}

    
<br>

### deregister

> **POST** /cost-analysis/v1/data-source/deregister
>




 {{< tabs " deregister " >}}




{{< /tabs >}}

    
<br>

### sync

> **POST** /cost-analysis/v1/data-source/sync
>




 {{< tabs " sync " >}}




{{< /tabs >}}

    
<br>

### get

> **POST** /cost-analysis/v1/data-source/get
>




 {{< tabs " get " >}}




{{< /tabs >}}

    
<br>

### list

> **POST** /cost-analysis/v1/data-source/list
>




 {{< tabs " list " >}}




{{< /tabs >}}

    
<br>

### stat

> **POST** /cost-analysis/v1/data-source/stat
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

    
* **data_source_type** (DataSourceType)  `Required` 

    
* **provider** (string)  `Required` 

    
* **plugin_info** (PluginInfo)  `Required` 

    
* **template** (Struct)  `Required` 

    
* **tags** (Struct)  `Required` 

    
* **cost_tag_keys** (string)  `Required` 

    
* **cost_additional_info_keys** (string)  `Required` 

    
* **domain_id** (string)  `Required` 

    
* **created_at** (string)  `Required` 

    
* **last_synchronized_at** (string)  `Required` 

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

    
* **data_source_type** (DataSourceType)  `Required` 

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

### PluginInfo
* **plugin_id** (string)  `Required` 

    
* **version** (string)  `Required` 

    
* **options** (Struct)  `Required` 

    
* **metadata** (Struct)  `Required` 

    
* **secret_data** (Struct)  `Required` 

    
* **schema** (string)  `Required` 

    
* **secret_id** (string)  `Required` 

    
* **upgrade_mode** (UpgradeMode)  `Required` 

    <br>

### RegisterDataSourceRequest
* **name** (string)  `Required` 

  *is_required: true*

    
* **data_source_type** (DataSourceType)  `Required` 

  *is_required: true*

    
* **provider** (string)  `Required` 

  *is_required: false*

    
* **template** (Struct)  `Required` 

  *is_required: false*

    
* **plugin_info** (PluginInfo)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>

### SyncDataSourceRequest
* **data_source_id** (string)  `Required` 

  *is_required: true*

    
* **start** (string)  `Required` 

  *is_required: false*

    
* **no_preload_cache** (bool)  `Required` 

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

    
* **template** (Struct)  `Required` 

  *is_required: false*

    
* **tags** (Struct)  `Required` 

  *is_required: false*

    
* **domain_id** (string)  `Required` 

  *is_required: true*

    <br>
