---
description: A DataSource is a plugin instance collecting `metric` and `log` data from Cloudforet.
---
# Data source

>  **Package : spaceone.api.monitoring.v1**

## DataSource

{% hint style="info" %}
**DataSource Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**register**](data-source.md#register)|   [RegisterDataSourceRequest](data-source.md#registerdatasourcerequest) |   [DataSourceInfo](data-source.md#datasourceinfo) |
| [**update**](data-source.md#update)|   [UpdateDataSourceRequest](data-source.md#updatedatasourcerequest) |   [DataSourceInfo](data-source.md#datasourceinfo) |
| [**enable**](data-source.md#enable)|   [DataSourceRequest](data-source.md#datasourcerequest) |   [DataSourceInfo](data-source.md#datasourceinfo) |
| [**disable**](data-source.md#disable)|   [DataSourceRequest](data-source.md#datasourcerequest) |   [DataSourceInfo](data-source.md#datasourceinfo) |
| [**deregister**](data-source.md#deregister)|   [DataSourceRequest](data-source.md#datasourcerequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**update_plugin**](data-source.md#update_plugin)|   [UpdateDataSourcePluginRequest](data-source.md#updatedatasourcepluginrequest) |   [DataSourceInfo](data-source.md#datasourceinfo) |
| [**verify_plugin**](data-source.md#verify_plugin)|   [DataSourceRequest](data-source.md#datasourcerequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**get**](data-source.md#get)|   [GetDataSourceRequest](data-source.md#getdatasourcerequest) |   [DataSourceInfo](data-source.md#datasourceinfo) |
| [**list**](data-source.md#list)|   [DataSourceQuery](data-source.md#datasourcequery) |   [DataSourcesInfo](data-source.md#datasourcesinfo) |
| [**stat**](data-source.md#stat)|   [DataSourceStatQuery](data-source.md#datasourcestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### register
> **POST** /monitoring/v1/data-source/register
>

> Registers a DataSource with information of the plugin to use. Information of the plugin includes `version`, `provider`, `upgrade_mode`.

| Type | Message |
| :--- | :--- |
| Request | [RegisterDataSourceRequest](data-source.md#registerdatasourcerequest) |
| Response |  [DataSourceInfo](data-source.md#datasourceinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "name": "datasource-test",
    "plugin_info": {
        "plugin_id": "plugin-123456789012",
        "version": "1.1.4.20220617.135934",
        "options": {},
        "provider": "aws",
        "metadata": {
            "supported_resource_type": [
                "inventory.Server",
                "inventory.CloudService"
            ],
            "required_keys": [
                "data.cloudwatch"
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
        "a": "b"
    },
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
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
```
{% endtab %}
{% endtabs %}
 
 

 
### update
> **POST** /monitoring/v1/data-source/update
>

> Updates a specific DataSource. You can make changes in DataSource settings, including `name` and `tags`.

| Type | Message |
| :--- | :--- |
| Request | [UpdateDataSourceRequest](data-source.md#updatedatasourcerequest) |
| Response |  [DataSourceInfo](data-source.md#datasourceinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "data_source_id": "ds-123456789012",
    "name": "tmp-datasource_test",
    "tags": {
        "b": "c"
    },
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
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
```
{% endtab %}
{% endtabs %}
 
 

 
### enable
> **POST** /monitoring/v1/data-source/enable
>

> Enables a specific DataSource. By enabling a DataSource, you can communicate with an external cloud service via the plugin.

| Type | Message |
| :--- | :--- |
| Request | [DataSourceRequest](data-source.md#datasourcerequest) |
| Response |  [DataSourceInfo](data-source.md#datasourceinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "data_source_id": "ds-6167ed6b42f4",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
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
```
{% endtab %}
{% endtabs %}
 
 

 
### disable
> **POST** /monitoring/v1/data-source/disable
>

> Disables a specific DataSource. By disabling a DataSource, you can block communication with an external cloud service via the plugin.

| Type | Message |
| :--- | :--- |
| Request | [DataSourceRequest](data-source.md#datasourcerequest) |
| Response |  [DataSourceInfo](data-source.md#datasourceinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "data_source_id": "ds-6167ed6b42f4",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
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
```
{% endtab %}
{% endtabs %}
 
 

 
### deregister
> **POST** /monitoring/v1/data-source/deregister
>

> Deregisters and deletes a specific DataSource. You must specify the `data_source_id` of the DataSource to deregister.

| Type | Message |
| :--- | :--- |
| Request | [DataSourceRequest](data-source.md#datasourcerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "data_source_id": "ds-6167ed6b42f4",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### update_plugin
> **POST** /monitoring/v1/data-source/update-plugin
>

> Updates the plugin of a specific DataSource. This method resets the plugin data in the DataSource to update the `metadata`.

| Type | Message |
| :--- | :--- |
| Request | [UpdateDataSourcePluginRequest](data-source.md#updatedatasourcepluginrequest) |
| Response |  [DataSourceInfo](data-source.md#datasourceinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "data_source_id": "ds-6167ed6b42f4",
    "version": "1.1.3",
    "options": {},
    "upgrade_mode": "MANUAL",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
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
```
{% endtab %}
{% endtabs %}
 
 

 
### verify_plugin
> **POST** /monitoring/v1/data-source/verify-plugin
>

> Verifies the plugin of a specific DataSource. This method validates the plugin data, `version` and `endpoint`.

| Type | Message |
| :--- | :--- |
| Request | [DataSourceRequest](data-source.md#datasourcerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "data_source_id": "ds-6167ed6b42f4",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### get
> **POST** /monitoring/v1/data-source/get
>

> Gets a specific DataSource. Prints detailed information about the DataSource, including `name`, `state`, and `plugin_info`.

| Type | Message |
| :--- | :--- |
| Request | [GetDataSourceRequest](data-source.md#getdatasourcerequest) |
| Response |  [DataSourceInfo](data-source.md#datasourceinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "data_source_id": "ds-123456789012",
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
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
```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **POST** /monitoring/v1/data-source/list
>

> Gets a list of all DataSources. You can use a query to get a filtered list of DataSources.

| Type | Message |
| :--- | :--- |
| Request | [DataSourceQuery](data-source.md#datasourcequery) |
| Response |  [DataSourcesInfo](data-source.md#datasourcesinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "query": {},
    "domain_id": "domain-123456789012"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
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
```
{% endtab %}
{% endtabs %}
 
 

 
### stat
> **POST** /monitoring/v1/data-source/stat
>


| Type | Message |
| :--- | :--- |
| Request | [DataSourceStatQuery](data-source.md#datasourcestatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |


## 

## Message

### DataSourceInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">data_source_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">monitoring_type</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>METRIC</li>
          	<li>LOG</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">provider</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">capability</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">plugin_info</td>
      <td style="text-align:left"><a href="data-source.md#datasourceplugininfo">DataSourcePluginInfo</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### DataSourcePluginInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">plugin_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">version</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">options</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">metadata</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">upgrade_mode</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>MANUAL</li>
          	<li>AUTO</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">secret_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">provider</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### DataSourceQuery
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">query</td>
      <td style="text-align:left"><a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">data_source_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">monitoring_type</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>METRIC</li>
          	<li>LOG</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">provider</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### DataSourceRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| data_source_id |string|✔| |
| domain_id |string|✔| |

### DataSourceStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### DataSourcesInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of DataSourceInfo](data-source.md#datasourceinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### GetDataSourceRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| data_source_id |string|✔| |
| domain_id |string|✔| |
| only |list of string|✘| |

### RegisterDataSourceRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✔| |
| plugin_info |[DataSourcePluginInfo](data-source.md#datasourceplugininfo)|✔| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |

### UpdateDataSourcePluginRequest
<table>
  <thead>
    <tr>
      <th style="text-align:left; width:100px;">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:center">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left; width:100px;">data_source_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">version</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">options</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">upgrade_mode</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>MANUAL</li>
          	<li>AUTO</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
  </tbody>
</table>



### UpdateDataSourceRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| data_source_id |string|✔| |
| name |string|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |
