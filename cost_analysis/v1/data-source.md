---
description: A DataSource is a plugin instance collecting external cost data. External cost data consists of `raw data` and the plugin information used for collection.
---
# Data source

>  **Package : spaceone.api.cost_analysis.v1**

## DataSource

{% hint style="info" %}
**DataSource Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**register**](data-source.md#register)|   [RegisterDataSourceRequest](data-source.md#registerdatasourcerequest) |   [DataSourceInfo](data-source.md#datasourceinfo) |
| [**update**](data-source.md#update)|   [UpdateDataSourceRequest](data-source.md#updatedatasourcerequest) |   [DataSourceInfo](data-source.md#datasourceinfo) |
| [**update_plugin**](data-source.md#update_plugin)|   [UpdateDataSourcePluginRequest](data-source.md#updatedatasourcepluginrequest) |   [DataSourceInfo](data-source.md#datasourceinfo) |
| [**verify_plugin**](data-source.md#verify_plugin)|   [DataSourceRequest](data-source.md#datasourcerequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**enable**](data-source.md#enable)|   [DataSourceRequest](data-source.md#datasourcerequest) |   [DataSourceInfo](data-source.md#datasourceinfo) |
| [**disable**](data-source.md#disable)|   [DataSourceRequest](data-source.md#datasourcerequest) |   [DataSourceInfo](data-source.md#datasourceinfo) |
| [**deregister**](data-source.md#deregister)|   [DataSourceRequest](data-source.md#datasourcerequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**sync**](data-source.md#sync)|   [SyncDataSourceRequest](data-source.md#syncdatasourcerequest) |  JobInfo|
| [**get**](data-source.md#get)|   [GetDataSourceRequest](data-source.md#getdatasourcerequest) |   [DataSourceInfo](data-source.md#datasourceinfo) |
| [**list**](data-source.md#list)|   [DataSourceQuery](data-source.md#datasourcequery) |   [DataSourcesInfo](data-source.md#datasourcesinfo) |
| [**stat**](data-source.md#stat)|   [DataSourceStatQuery](data-source.md#datasourcestatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)| 
 

 
### register
> **POST** /cost-analysis/v1/data-source/register
>

> Registers a DataSource with information of the plugin to use. Information of the plugin includes `version`, `provider`, and `upgrade_mode`.

| Type | Message |
| :--- | :--- |
| Request | [RegisterDataSourceRequest](data-source.md#registerdatasourcerequest) |
| Response |  [DataSourceInfo](data-source.md#datasourceinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "name": "AWS HyperBilling Data Source test",
    "data_source_type": "EXTERNAL",
    "plugin_info": {
        "plugin_id": "plugin-aws-hyperbilling-cost-datasource",
        "version": "1.0.4",
        "options": {},
        "metadata": {
            "data_source_rules": [
                {
                    "conditions_policy": "ALWAYS",
                    "options": {
                        "stop_processing": true
                    },
                    "actions": {
                        "match_service_account": {
                            "source": "account",
                            "target": "data.account_id"
                        }
                    },
                    "conditions": [],
                    "tags": {},
                    "name": "match_service_account"
                }
            ]
        },
        "secret_id": "secret-ca134639483",
        "upgrade_mode": "AUTO"
    },
    "tags": {
        "a": "b"
    }
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "data_source_id": "ds-085d1e872789",
    "name": "AWS HyperBilling Data Source test",
    "state": "ENABLED",
    "data_source_type": "EXTERNAL",
    "plugin_info": {
        "plugin_id": "plugin-aws-hyperbilling-cost-datasource",
        "version": "1.0.4",
        "options": {},
        "metadata": {
            "data_source_rules": [
                {
                    "options": {
                        "stop_processing": true
                    },
                    "actions": {
                        "match_service_account": {
                            "source": "account",
                            "target": "data.account_id"
                        }
                    },
                    "domain_id": "domain-58010aa2e451",
                    "conditions": [],
                    "name": "match_service_account",
                    "tags": {},
                    "data_source_id": "ds-085d1e872789",
                    "conditions_policy": "ALWAYS"
                }
            ]
        },
        "secret_id": "secret-ca134639483",
        "upgrade_mode": "AUTO"
    },
    "template": {},
    "tags": {
        "a": "b"
    },
    "cost_tag_keys": [
        "Name",
        "Environment",
        "Role",
        "Service"
    ],
    "cost_additional_info_keys": [
        "raw_usage_type"
    ],
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-07-19T10:58:36.080Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### update
> **POST** /cost-analysis/v1/data-source/update
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
    "data_source_id": "ds-085d1e872789",
    "name": "AWS HyperBilling Data Source test2",
    "tags": {
        "type": "test"
    }
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "data_source_id": "ds-085d1e872789",
    "name": "AWS HyperBilling Data Source test2",
    "state": "ENABLED",
    "data_source_type": "EXTERNAL",
    "plugin_info": {
        "plugin_id": "plugin-aws-hyperbilling-cost-datasource",
        "version": "1.0.4",
        "options": {},
        "metadata": {
            "data_source_rules": [
                {
                    "tags": {},
                    "name": "match_service_account",
                    "conditions_policy": "ALWAYS",
                    "actions": {
                        "match_service_account": {
                            "target": "data.account_id",
                            "source": "account"
                        }
                    },
                    "options": {
                        "stop_processing": true
                    },
                    "conditions": []
                }
            ]
        },
        "secret_id": "secret-dca385e85a27",
        "upgrade_mode": "AUTO"
    },
    "template": {},
    "tags": {
        "type": "test"
    },
    "cost_tag_keys": [
        "Name",
        "Environment",
        "Role",
        "Service"
    ],
    "cost_additional_info_keys": [
        "raw_usage_type"
    ],
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-07-19T10:58:36.080Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### update_plugin
> **POST** /cost-analysis/v1/data-source/update-plugin
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
    "data_source_id": "ds-085d1e872789",
    "version": "1.0.4",
    "options": {},
    "upgrade_mode": "AUTO"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "data_source_id": "ds-085d1e872789",
    "name": "AWS HyperBilling Data Source test2",
    "state": "DISABLED",
    "data_source_type": "EXTERNAL",
    "plugin_info": {
        "plugin_id": "plugin-aws-hyperbilling-cost-datasource",
        "version": "1.0.4",
        "options": {},
        "metadata": {
            "data_source_rules": [
                {
                    "tags": {},
                    "actions": {
                        "match_service_account": {
                            "source": "account",
                            "target": "data.account_id"
                        }
                    },
                    "options": {
                        "stop_processing": true
                    },
                    "conditions_policy": "ALWAYS",
                    "name": "match_service_account",
                    "conditions": []
                }
            ]
        },
        "secret_id": "secret-dca385e85a27",
        "upgrade_mode": "AUTO"
    },
    "template": {},
    "tags": {
        "type": "test"
    },
    "cost_tag_keys": [
        "Name",
        "Environment",
        "Role",
        "Service"
    ],
    "cost_additional_info_keys": [
        "raw_usage_type"
    ],
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-07-19T10:58:36.080Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### verify_plugin
> **POST** /cost-analysis/v1/data-source/verify-plugin
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
    "data_source_id": "ds-085d1e872789"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### enable
> **POST** /cost-analysis/v1/data-source/enable
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
    "data_source_id": "ds-085d1e872789"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "data_source_id": "ds-085d1e872789",
    "name": "AWS HyperBilling Data Source test2",
    "state": "ENABLED",
    "data_source_type": "EXTERNAL",
    "plugin_info": {
        "plugin_id": "plugin-aws-hyperbilling-cost-datasource",
        "version": "1.0.4",
        "options": {},
        "metadata": {
            "data_source_rules": [
                {
                    "actions": {
                        "match_service_account": {
                            "target": "data.account_id",
                            "source": "account"
                        }
                    },
                    "conditions_policy": "ALWAYS",
                    "conditions": [],
                    "options": {
                        "stop_processing": true
                    },
                    "name": "match_service_account",
                    "tags": {}
                }
            ]
        },
        "secret_id": "secret-dca385e85a27",
        "upgrade_mode": "AUTO"
    },
    "template": {},
    "tags": {
        "type": "test"
    },
    "cost_tag_keys": [
        "Name",
        "Environment",
        "Role",
        "Service"
    ],
    "cost_additional_info_keys": [
        "raw_usage_type"
    ],
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-07-19T10:58:36.080Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### disable
> **POST** /cost-analysis/v1/data-source/disable
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
    "data_source_id": "ds-085d1e872789"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "data_source_id": "ds-085d1e872789",
    "name": "AWS HyperBilling Data Source test2",
    "state": "DISABLED",
    "data_source_type": "EXTERNAL",
    "plugin_info": {
        "plugin_id": "plugin-aws-hyperbilling-cost-datasource",
        "version": "1.0.4",
        "options": {},
        "metadata": {
            "data_source_rules": [
                {
                    "name": "match_service_account",
                    "options": {
                        "stop_processing": true
                    },
                    "conditions_policy": "ALWAYS",
                    "conditions": [],
                    "actions": {
                        "match_service_account": {
                            "source": "account",
                            "target": "data.account_id"
                        }
                    },
                    "tags": {}
                }
            ]
        },
        "secret_id": "secret-dca385e85a27",
        "upgrade_mode": "AUTO"
    },
    "template": {},
    "tags": {
        "type": "test"
    },
    "cost_tag_keys": [
        "Name",
        "Environment",
        "Role",
        "Service"
    ],
    "cost_additional_info_keys": [
        "raw_usage_type"
    ],
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-07-19T10:58:36.080Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### deregister
> **POST** /cost-analysis/v1/data-source/deregister
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
    "data_source_id": "ds-085d1e872789"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### sync
> **POST** /cost-analysis/v1/data-source/sync
>

> Manually runs a specific DataSource to collect the cost data. This method is to get up-to-date cost data.

| Type | Message |
| :--- | :--- |
| Request | [SyncDataSourceRequest](data-source.md#syncdatasourcerequest) |
| Response | JobInfo |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "data_source_id": "ds-c96609f5afeb"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "job_id": "job-ba2598167785",
    "status": "IN_PROGRESS",
    "options": {
        "no_preload_cache": false,
        "start": null
    },
    "total_tasks": 1,
    "remained_tasks": 1,
    "data_source_id": "ds-c96609f5afeb",
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-07-19T11:16:59.923Z",
    "updated_at": "2022-07-19T11:16:59.923Z",
    "changed": [
        {
            "start": "2022-07-01T00:00:00.000Z"
        }
    ]
}
```
{% endtab %}
{% endtabs %}
 
 

 
### get
> **POST** /cost-analysis/v1/data-source/get
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
    "data_source_id": "ds-fcba92ca73b1"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "data_source_id": "ds-fcba92ca73b1",
    "name": "AWS HyperBilling Data Source",
    "state": "ENABLED",
    "data_source_type": "EXTERNAL",
    "plugin_info": {
        "plugin_id": "plugin-aws-hyperbilling-cost-datasource",
        "version": "1.0.4",
        "options": {},
        "metadata": {
            "data_source_rules": [
                {
                    "conditions_policy": "ALWAYS",
                    "options": {
                        "stop_processing": true
                    },
                    "tags": {},
                    "conditions": [],
                    "name": "match_service_account",
                    "actions": {
                        "match_service_account": {
                            "source": "account",
                            "target": "data.account_id"
                        }
                    }
                }
            ]
        },
        "secret_id": "secret-dca385e85a27",
        "upgrade_mode": "AUTO"
    },
    "template": {},
    "tags": {
        "a": "b"
    },
    "cost_tag_keys": [
        "Name",
        "Environment",
        "Role",
        "Service"
    ],
    "cost_additional_info_keys": [
        "raw_usage_type"
    ],
    "domain_id": "domain-58010aa2e451",
    "created_at": "2022-03-30T02:21:28.756Z",
    "last_synchronized_at": "2022-07-17T16:00:05.077Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **POST** /cost-analysis/v1/data-source/list
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
    "query": {}
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "results": [
        {
            "data_source_id": "ds-fcba92ca73b1",
            "name": "AWS HyperBilling Data Source",
            "state": "ENABLED",
            "data_source_type": "EXTERNAL",
            "plugin_info": {
                "plugin_id": "plugin-aws-hyperbilling-cost-datasource",
                "version": "1.0.4",
                "options": {},
                "metadata": {
                    "data_source_rules": [
                        {
                            "name": "match_service_account",
                            "conditions": [],
                            "actions": {
                                "match_service_account": {
                                    "source": "account",
                                    "target": "data.account_id"
                                }
                            },
                            "conditions_policy": "ALWAYS",
                            "tags": {},
                            "options": {
                                "stop_processing": true
                            }
                        }
                    ]
                },
                "secret_id": "secret-dca385e85a27",
                "upgrade_mode": "AUTO"
            },
            "template": {},
            "tags": {
                "a": "b"
            },
            "cost_tag_keys": [
                "Name",
                "Environment",
                "Role",
                "Service"
            ],
            "cost_additional_info_keys": [
                "raw_usage_type"
            ],
            "domain_id": "domain-58010aa2e451",
            "created_at": "2022-03-30T02:21:28.756Z",
            "last_synchronized_at": "2022-07-17T16:00:05.077Z"
        },
        {
            "data_source_id": "ds-c96609f5afeb",
            "name": "MZC HyperBilling Data Source",
            "state": "ENABLED",
            "data_source_type": "EXTERNAL",
            "plugin_info": {
                "plugin_id": "plugin-mzc-hyperbilling-cost-datasource",
                "version": "1.0.3",
                "options": {},
                "metadata": {
                    "data_source_rules": [
                        {
                            "conditions": [],
                            "options": {
                                "stop_processing": true
                            },
                            "conditions_policy": "ALWAYS",
                            "name": "match_service_account",
                            "tags": {},
                            "actions": {
                                "match_service_account": {
                                    "source": "account",
                                    "target": "data.project_id"
                                }
                            }
                        }
                    ]
                },
                "secret_id": "secret-354d142229e5",
                "upgrade_mode": "AUTO"
            },
            "template": {},
            "tags": {},
            "cost_tag_keys": [],
            "cost_additional_info_keys": [],
            "domain_id": "domain-58010aa2e451",
            "created_at": "2022-04-13T05:34:54.223Z",
            "last_synchronized_at": "2022-07-17T16:00:08.254Z"
        }
    ],
    "total_count": 2
}
```
{% endtab %}
{% endtabs %}
 
 

 
### stat
> **POST** /cost-analysis/v1/data-source/stat
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
          	<li>STATE_NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">data_source_type</td>
      <td style="text-align:left"><ul>
          	<li>TYPE_NONE</li>
          	<li>LOCAL</li>
          	<li>EXTERNAL</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">provider</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">plugin_info</td>
      <td style="text-align:left"><a href="data-source.md#plugininfo">PluginInfo</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">template</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">cost_tag_keys</td>
      <td style="text-align:left">list of string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">cost_additional_info_keys</td>
      <td style="text-align:left">list of string</td>
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
    <tr>
      <td style="text-align:left; width:100px;">last_synchronized_at</td>
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
      <td style="text-align:left; width:100px;">data_source_type</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>LOCAL</li>
          	<li>EXTERNAL</li>
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

### PluginInfo
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
      <td style="text-align:left; width:100px;">secret_data</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">schema</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">secret_id</td>
      <td style="text-align:left">string</td>
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
  </tbody>
</table>



### RegisterDataSourceRequest
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
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">data_source_type</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>LOCAL</li>
          	<li>EXTERNAL</li>
        </ul></td>
<td style="text-align:center">✔</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">provider</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">template</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">plugin_info</td>
      <td style="text-align:left"><a href="data-source.md#plugininfo">PluginInfo</a></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
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



### SyncDataSourceRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| data_source_id |string|✔| |
| start |string|✘| |
| no_preload_cache |bool|✘| |
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
| template |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |
