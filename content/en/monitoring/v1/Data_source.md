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

desc: Registers a DataSource with information of the plugin to use. Information of the plugin includes `version`, `provider`, `upgrade_mode`.
request_example: >-
{
"name": "datasource-test",
"plugin_info": {"plugin_id": "plugin-123456789012",
"version": "1.1.4.20220617.135934",
"options": {},
"provider": "aws",
"metadata": {
"supported_resource_type": ["inventory.Server", "inventory.CloudService"],
"required_keys": ["data.cloudwatch"],
"supported_stat": ["AVERAGE", "MAX", "MIN", "SUM"]},
"upgrade_mode": "AUTO"
},
"tags": {"a": "b"},
"domain_id": "domain-123456789012"
}
response_example: >-
{
"data_source_id": "ds-123456789012",
"name": "datasource-test",
"state": "ENABLED",
"monitoring_type": "METRIC",
"provider": "aws",
"capability": {
"supported_schema": [
"aws_access_key",
"aws_assume_role"
],
"use_resource_secret": true,
"monitoring_type": "METRIC"
},
"plugin_info": {
"plugin_id": "plugin-123456789012",
"version": "1.1.4.20220617.135934",
"options": {},
"provider": "aws",
"metadata": {
"supported_stat": [
"AVERAGE",
"MAX",
"MIN",
"SUM"
],
"supported_resource_type": [
"inventory.Server",
"inventory.CloudService"
],
"required_keys": [
"data.cloudwatch"
]
},
"upgrade_mode": "AUTO"
},
"tags": {
"a": "b"
},
"domain_id": "domain-123456789012",
"created_at": "2022-06-21T01:17:12.144Z"
}



> **POST** /monitoring/v1/data-source/register
>






    
<br>

### update

desc: Updates a specific DataSource. You can make changes in DataSource settings, including `name` and `tags`.
request_example: >-
{
"data_source_id": "ds-123456789012",
"name": "tmp-datasource_test",
"tags": {"b": "c"},
"domain_id": "domain-123456789012"
}
response_example: >-
{
"data_source_id": "ds-123456789012",
"name": "tmp-datasource_test",
"state": "ENABLED",
"monitoring_type": "METRIC",
"provider": "aws",
"capability": {
"use_resource_secret": true,
"monitoring_type": "METRIC",
"supported_schema": [
"aws_access_key",
"aws_assume_role"
]
},
"plugin_info": {
"plugin_id": "plugin-123456789012",
"version": "1.1.4.20220617.135934",
"options": {},
"provider": "aws",
"metadata": {
"required_keys": [
"data.cloudwatch"
],
"supported_resource_type": [
"inventory.Server",
"inventory.CloudService"
],
"supported_stat": [
"AVERAGE",
"MAX",
"MIN",
"SUM"
]
},
"upgrade_mode": "AUTO"
},
"tags": {
"b": "c"
},
"domain_id": "domain-123456789012",
"created_at": "2022-06-21T01:17:12.144Z"
}



> **POST** /monitoring/v1/data-source/update
>






    
<br>

### enable

desc: Enables a specific DataSource. By enabling a DataSource, you can communicate with an external cloud service via the plugin.
request_example: >-
{
"data_source_id": "ds-6167ed6b42f4",
"domain_id": "domain-123456789012"
}
response_example: >-
{
"data_source_id": "ds-6167ed6b42f4",
"name": "tmp-datasource_test",
"state": "ENABLED",
"monitoring_type": "METRIC",
"provider": "aws",
"capability": {
"supported_schema": [
"aws_access_key",
"aws_assume_role"
],
"monitoring_type": "METRIC",
"use_resource_secret": true
},
"plugin_info": {
"plugin_id": "plugin-5cdf8d72a7cc",
"version": "1.1.4.20220617.135934",
"options": {},
"provider": "aws",
"metadata": {
"supported_stat": [
"AVERAGE",
"MAX",
"MIN",
"SUM"
],
"required_keys": [
"data.cloudwatch"
],
"supported_resource_type": [
"inventory.Server",
"inventory.CloudService"
]
},
"upgrade_mode": "AUTO"
},
"tags": {
"b": "c"
},
"domain_id": "domain-123456789012",
"created_at": "2022-06-21T01:17:12.144Z"
}



> **POST** /monitoring/v1/data-source/enable
>






    
<br>

### disable

desc: Disables a specific DataSource. By disabling a DataSource, you can block communication with an external cloud service via the plugin.
request_example: >-
{
"data_source_id": "ds-6167ed6b42f4",
"domain_id": "domain-123456789012"
}
response_example: >-
{
"data_source_id": "ds-6167ed6b42f4",
"name": "tmp-datasource_test",
"state": "DISABLED",
"monitoring_type": "METRIC",
"provider": "aws",
"capability": {
"supported_schema": [
"aws_access_key",
"aws_assume_role"
],
"monitoring_type": "METRIC",
"use_resource_secret": true
},
"plugin_info": {
"plugin_id": "plugin-5cdf8d72a7cc",
"version": "1.1.4.20220617.135934",
"options": {},
"provider": "aws",
"metadata": {
"supported_stat": [
"AVERAGE",
"MAX",
"MIN",
"SUM"
],
"required_keys": [
"data.cloudwatch"
],
"supported_resource_type": [
"inventory.Server",
"inventory.CloudService"
]
},
"upgrade_mode": "AUTO"
},
"tags": {
"b": "c"
},
"domain_id": "domain-123456789012",
"created_at": "2022-06-21T01:17:12.144Z"
}



> **POST** /monitoring/v1/data-source/disable
>






    
<br>

### deregister

desc: Deregisters and deletes a specific DataSource. You must specify the `data_source_id` of the DataSource to deregister.
request_example: >-
{
"data_source_id": "ds-6167ed6b42f4",
"domain_id": "domain-123456789012"
}



> **POST** /monitoring/v1/data-source/deregister
>






    
<br>

### update_plugin

desc: Updates the plugin of a specific DataSource. This method resets the plugin data in the DataSource to update the `metadata`.
request_example: >-
{
"data_source_id": "ds-6167ed6b42f4",
"version": "1.1.3",
"options": {},
"upgrade_mode": "MANUAL",
"domain_id": "domain-123456789012"
}
response_example: >-
{
"data_source_id": "ds-6167ed6b42f4",
"name": "tmp-datasource_test",
"state": "ENABLED",
"monitoring_type": "METRIC",
"provider": "aws",
"capability": {
"use_resource_secret": true,
"supported_schema": [
"aws_access_key",
"aws_assume_role"
],
"monitoring_type": "METRIC"
},
"plugin_info": {
"plugin_id": "plugin-5cdf8d72a7cc",
"version": "1.1.3",
"options": {},
"provider": "aws",
"metadata": {
"required_keys": [
"data.cloudwatch"
],
"supported_resource_type": [
"inventory.Server",
"inventory.CloudService"
],
"supported_stat": [
"AVERAGE",
"MAX",
"MIN",
"SUM"
]
},
"upgrade_mode": "MANUAL"
},
"tags": {
"b": "c"
},
"domain_id": "domain-123456789012",
"created_at": "2022-06-21T01:17:12.144Z"
}



> **POST** /monitoring/v1/data-source/update-plugin
>






    
<br>

### verify_plugin

desc: Verifies the plugin of a specific DataSource. This method validates the plugin data, `version` and `endpoint`.
request_example: >-
{
"data_source_id": "ds-6167ed6b42f4",
"domain_id": "domain-123456789012"
}



> **POST** /monitoring/v1/data-source/verify-plugin
>






    
<br>

### get

desc: Gets a specific DataSource. Prints detailed information about the DataSource, including `name`, `state`, and `plugin_info`.
request_example: >-
{
"data_source_id": "ds-123456789012",
"domain_id": "domain-123456789012"
}
response_example: >-
{
"data_source_id": "ds-89f1e81528e9",
"name": "AWS CloudTrail",
"state": "ENABLED",
"monitoring_type": "LOG",
"provider": "aws",
"capability": {
"use_resource_secret": true,
"supported_schema": [
"aws_access_key",
"aws_assume_role"
],
"monitoring_type": "LOG"
},
"plugin_info": {
"plugin_id": "plugin-9881b9b440a4",
"version": "1.0-dev2",
"options": {},
"provider": "aws",
"metadata": {
"supported_resource_type": [
"inventory.Server",
"inventory.CloudService"
],
"required_keys": [
"reference.resource_id"
]
},
"upgrade_mode": "AUTO"
},
"tags": {},
"domain_id": "domain-123456789012",
"created_at": "2021-03-31T08:39:45.532Z"
}



> **POST** /monitoring/v1/data-source/get
>






    
<br>

### list

desc: Gets a list of all DataSources. You can use a query to get a filtered list of DataSources.
request_example: >-
{
"query": {},
"domain_id": "domain-123456789012"
}
response_example: >-
{
"results": [
{
"data_source_id": "ds-89f1e81528e9",
"name": "AWS CloudTrail",
"state": "ENABLED",
"monitoring_type": "LOG",
"provider": "aws",
"capability": {
"use_resource_secret": true,
"monitoring_type": "LOG",
"supported_schema": [
"aws_access_key",
"aws_assume_role"
]
},
"plugin_info": {
"plugin_id": "plugin-9881b9b440a4",
"version": "1.0-dev2",
"options": {},
"provider": "aws",
"metadata": {
"required_keys": [
"reference.resource_id"
],
"supported_resource_type": [
"inventory.Server",
"inventory.CloudService"
]
},
"upgrade_mode": "AUTO"
},
"tags": {},
"domain_id": "domain-123456789012",
"created_at": "2021-03-31T08:39:45.532Z"
}
],
"total_count": 2
}



> **POST** /monitoring/v1/data-source/list
>






    
<br>

### stat





> **POST** /monitoring/v1/data-source/stat
>






    


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
