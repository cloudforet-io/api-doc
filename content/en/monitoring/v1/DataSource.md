---
title: "DataSource"
linkTitle: "DataSource"
weight: 3
bookFlatSection: true
---
# [DataSource](#DataSource)
A DataSource is a plugin instance collecting `metric` and `log` data from Cloudforet.


>  **Package : spaceone.api.monitoring.v1**

<br>
<br>

## DataSource





**DataSource Methods:**


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**register**](./DataSource#register) | [RegisterDataSourceRequest](DataSource#registerdatasourcerequest) | [DataSourceInfo](DataSource#datasourceinfo) |
| [**update**](./DataSource#update) | [UpdateDataSourceRequest](DataSource#updatedatasourcerequest) | [DataSourceInfo](DataSource#datasourceinfo) |
| [**enable**](./DataSource#enable) | [DataSourceRequest](DataSource#datasourcerequest) | [DataSourceInfo](DataSource#datasourceinfo) |
| [**disable**](./DataSource#disable) | [DataSourceRequest](DataSource#datasourcerequest) | [DataSourceInfo](DataSource#datasourceinfo) |
| [**deregister**](./DataSource#deregister) | [DataSourceRequest](DataSource#datasourcerequest) | [Empty](DataSource#empty) |
| [**update_plugin**](./DataSource#update_plugin) | [UpdateDataSourcePluginRequest](DataSource#updatedatasourcepluginrequest) | [DataSourceInfo](DataSource#datasourceinfo) |
| [**verify_plugin**](./DataSource#verify_plugin) | [DataSourceRequest](DataSource#datasourcerequest) | [Empty](DataSource#empty) |
| [**get**](./DataSource#get) | [GetDataSourceRequest](DataSource#getdatasourcerequest) | [DataSourceInfo](DataSource#datasourceinfo) |
| [**list**](./DataSource#list) | [DataSourceQuery](DataSource#datasourcequery) | [DataSourcesInfo](DataSource#datasourcesinfo) |
| [**stat**](./DataSource#stat) | [DataSourceStatQuery](DataSource#datasourcestatquery) | [Struct](DataSource#struct) |



    
<br>

### register

Registers a DataSource with information of the plugin to use. Information of the plugin includes `version`, `provider`, `upgrade_mode`.



> **POST** /monitoring/v1/data-source/register
>





 {{< tabs " register " >}}

 {{< tab "Request Example" >}}



[RegisterDataSourceRequest](./DataSource#registerdatasourcerequest)

* **name** (string)   `Required` 


* **plugin_info** (DataSourcePluginInfo)   `Required` 


* **domain_id** (string)   `Required` 


* **tags** (Struct)  





{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[DataSourceInfo](#DATASOURCEINFO)
* **data_source_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **monitoring_type** (MonitoringType)   `Required` 

* **provider** (string)   `Required` 

* **capability** (Struct)   `Required` 

* **plugin_info** (DataSourcePluginInfo)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### update

Updates a specific DataSource. You can make changes in DataSource settings, including `name` and `tags`.



> **POST** /monitoring/v1/data-source/update
>





 {{< tabs " update " >}}

 {{< tab "Request Example" >}}



[UpdateDataSourceRequest](./DataSource#updatedatasourcerequest)

* **data_source_id** (string)   `Required` 


* **domain_id** (string)   `Required` 


* **name** (string)  


* **tags** (Struct)  





{{< highlight json >}}
{
       "data_source_id": "ds-123456789012",
       "name": "tmp-datasource_test",
       "tags": {"b": "c"},
       "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[DataSourceInfo](#DATASOURCEINFO)
* **data_source_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **monitoring_type** (MonitoringType)   `Required` 

* **provider** (string)   `Required` 

* **capability** (Struct)   `Required` 

* **plugin_info** (DataSourcePluginInfo)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### enable

Enables a specific DataSource. By enabling a DataSource, you can communicate with an external cloud service via the plugin.



> **POST** /monitoring/v1/data-source/enable
>





 {{< tabs " enable " >}}

 {{< tab "Request Example" >}}



[DataSourceRequest](./DataSource#datasourcerequest)

* **data_source_id** (string)   `Required` 


* **domain_id** (string)   `Required` 





{{< highlight json >}}
{
   "data_source_id": "ds-6167ed6b42f4",
   "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[DataSourceInfo](#DATASOURCEINFO)
* **data_source_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **monitoring_type** (MonitoringType)   `Required` 

* **provider** (string)   `Required` 

* **capability** (Struct)   `Required` 

* **plugin_info** (DataSourcePluginInfo)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### disable

Disables a specific DataSource. By disabling a DataSource, you can block communication with an external cloud service via the plugin.



> **POST** /monitoring/v1/data-source/disable
>





 {{< tabs " disable " >}}

 {{< tab "Request Example" >}}



[DataSourceRequest](./DataSource#datasourcerequest)

* **data_source_id** (string)   `Required` 


* **domain_id** (string)   `Required` 





{{< highlight json >}}
{
   "data_source_id": "ds-6167ed6b42f4",
   "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[DataSourceInfo](#DATASOURCEINFO)
* **data_source_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **monitoring_type** (MonitoringType)   `Required` 

* **provider** (string)   `Required` 

* **capability** (Struct)   `Required` 

* **plugin_info** (DataSourcePluginInfo)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### deregister

Deregisters and deletes a specific DataSource. You must specify the `data_source_id` of the DataSource to deregister.



> **POST** /monitoring/v1/data-source/deregister
>





 {{< tabs " deregister " >}}

 {{< tab "Request Example" >}}



[DataSourceRequest](./DataSource#datasourcerequest)

* **data_source_id** (string)   `Required` 


* **domain_id** (string)   `Required` 





{{< highlight json >}}
{
   "data_source_id": "ds-6167ed6b42f4",
   "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### update_plugin

Updates the plugin of a specific DataSource. This method resets the plugin data in the DataSource to update the `metadata`.



> **POST** /monitoring/v1/data-source/update-plugin
>





 {{< tabs " update_plugin " >}}

 {{< tab "Request Example" >}}



[UpdateDataSourcePluginRequest](./DataSource#updatedatasourcepluginrequest)

* **data_source_id** (string)   `Required` 


* **domain_id** (string)   `Required` 


* **version** (string)  


* **options** (Struct)  


* **upgrade_mode** (UpgradeMode)  





{{< highlight json >}}
{
   "data_source_id": "ds-6167ed6b42f4",
   "version": "1.1.3",
   "options": {},
   "upgrade_mode": "MANUAL",
   "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[DataSourceInfo](#DATASOURCEINFO)
* **data_source_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **monitoring_type** (MonitoringType)   `Required` 

* **provider** (string)   `Required` 

* **capability** (Struct)   `Required` 

* **plugin_info** (DataSourcePluginInfo)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### verify_plugin

Verifies the plugin of a specific DataSource. This method validates the plugin data, `version` and `endpoint`.



> **POST** /monitoring/v1/data-source/verify-plugin
>





 {{< tabs " verify_plugin " >}}

 {{< tab "Request Example" >}}



[DataSourceRequest](./DataSource#datasourcerequest)

* **data_source_id** (string)   `Required` 


* **domain_id** (string)   `Required` 





{{< highlight json >}}
{
   "data_source_id": "ds-6167ed6b42f4",
   "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}



{{< /tabs >}}


    
<br>

### get

Gets a specific DataSource. Prints detailed information about the DataSource, including `name`, `state`, and `plugin_info`.



> **POST** /monitoring/v1/data-source/get
>





 {{< tabs " get " >}}

 {{< tab "Request Example" >}}



[GetDataSourceRequest](./DataSource#getdatasourcerequest)

* **data_source_id** (string)   `Required` 


* **domain_id** (string)   `Required` 


* **only** (string)  `Repeated`   





{{< highlight json >}}
{
   "data_source_id": "ds-123456789012",
   "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[DataSourceInfo](#DATASOURCEINFO)
* **data_source_id** (string)   `Required` 

* **name** (string)   `Required` 

* **state** (State)   `Required` 

* **monitoring_type** (MonitoringType)   `Required` 

* **provider** (string)   `Required` 

* **capability** (Struct)   `Required` 

* **plugin_info** (DataSourcePluginInfo)   `Required` 

* **tags** (Struct)   `Required` 

* **domain_id** (string)   `Required` 

* **created_at** (string)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### list

Gets a list of all DataSources. You can use a query to get a filtered list of DataSources.



> **POST** /monitoring/v1/data-source/list
>





 {{< tabs " list " >}}

 {{< tab "Request Example" >}}



[DataSourceQuery](./DataSource#datasourcequery)

* **domain_id** (string)   `Required` 


* **query** (Query)  


* **data_source_id** (string)  


* **name** (string)  


* **state** (string)  


* **monitoring_type** (MonitoringType)  


* **provider** (string)  





{{< highlight json >}}
{
   "query": {},
   "domain_id": "domain-123456789012"
}
{{< /highlight >}}
{{< /tab >}}


 {{< tab "Response Example" >}}

[DataSourcesInfo](#DATASOURCESINFO)
* **results** (DataSourceInfo)  `Repeated`   `Required` 

* **total_count** (int32)   `Required` 



{{< highlight json >}}
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
{{< /highlight >}}
{{< /tab >}}


{{< /tabs >}}


    
<br>

### stat





> **POST** /monitoring/v1/data-source/stat
>






    


<br>
<br>

## Message



### DataSourceInfo
* **data_source_id** (string)   `Required` 

    
* **name** (string)   `Required` 

    
* **state** (State)   `Required` 

    
* **monitoring_type** (MonitoringType)   `Required` 

    
* **provider** (string)   `Required` 

    
* **capability** (Struct)   `Required` 

    
* **plugin_info** (DataSourcePluginInfo)   `Required` 

    
* **tags** (Struct)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **created_at** (string)   `Required` 

    <br>

### DataSourcePluginInfo
* **plugin_id** (string)   `Required` 

    
* **version** (string)   `Required` 

    
* **options** (Struct)   `Required` 

    
* **metadata** (Struct)   `Required` 

    
* **upgrade_mode** (UpgradeMode)   `Required` 

    
* **secret_id** (string)   `Required` 

    
* **provider** (string)   `Required` 

    <br>

### DataSourceQuery
* **domain_id** (string)   `Required` 

    
* **query** (Query)  

    
* **data_source_id** (string)  

    
* **name** (string)  

    
* **state** (string)  

    
* **monitoring_type** (MonitoringType)  

    
* **provider** (string)  

    <br>

### DataSourceRequest
* **data_source_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### DataSourceStatQuery
* **query** (StatisticsQuery)   `Required` 

    
* **domain_id** (string)   `Required` 

    <br>

### DataSourcesInfo
* **results** (DataSourceInfo)  `Repeated`    `Required` 

    
* **total_count** (int32)   `Required` 

    <br>

### GetDataSourceRequest
* **data_source_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **only** (string)  `Repeated`   

    <br>

### RegisterDataSourceRequest
* **name** (string)   `Required` 

    
* **plugin_info** (DataSourcePluginInfo)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **tags** (Struct)  

    <br>

### UpdateDataSourcePluginRequest
* **data_source_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **version** (string)  

    
* **options** (Struct)  

    
* **upgrade_mode** (UpgradeMode)  

    <br>

### UpdateDataSourceRequest
* **data_source_id** (string)   `Required` 

    
* **domain_id** (string)   `Required` 

    
* **name** (string)  

    
* **tags** (Struct)  

    <br>
