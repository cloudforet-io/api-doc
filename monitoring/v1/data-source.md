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
> **POST** /monitoring/v1/data-sources
>

> Registers a DataSource with information of the plugin to use. Information of the plugin includes `version`, `provider`, `upgrade_mode`.

| Type | Message |
| :--- | :--- |
| Request | [RegisterDataSourceRequest](data-source.md#registerdatasourcerequest) |
| Response |  [DataSourceInfo](data-source.md#datasourceinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text

```
{% endtab %}

{% tab title="Response Example" %}
```text

```
{% endtab %}
{% endtabs %}
 
 

 
### update
> **PUT** /monitoring/v1/data-source/{data_source_id}
>

> Updates a specific DataSource. You can make changes in DataSource settings, including `name` and `tags`.

| Type | Message |
| :--- | :--- |
| Request | [UpdateDataSourceRequest](data-source.md#updatedatasourcerequest) |
| Response |  [DataSourceInfo](data-source.md#datasourceinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text

```
{% endtab %}

{% tab title="Response Example" %}
```text

```
{% endtab %}
{% endtabs %}
 
 

 
### enable
> **PUT** /monitoring/v1/data-source/{data_source_id}/enable
>

> Enables a specific DataSource. By enabling a DataSource, you can communicate with an external cloud service via the plugin.

| Type | Message |
| :--- | :--- |
| Request | [DataSourceRequest](data-source.md#datasourcerequest) |
| Response |  [DataSourceInfo](data-source.md#datasourceinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text

```
{% endtab %}

{% tab title="Response Example" %}
```text

```
{% endtab %}
{% endtabs %}
 
 

 
### disable
> **PUT** /monitoring/v1/data-source/{data_source_id}/disable
>

> Disables a specific DataSource. By disabling a DataSource, you can block communication with an external cloud service via the plugin.

| Type | Message |
| :--- | :--- |
| Request | [DataSourceRequest](data-source.md#datasourcerequest) |
| Response |  [DataSourceInfo](data-source.md#datasourceinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text

```
{% endtab %}

{% tab title="Response Example" %}
```text

```
{% endtab %}
{% endtabs %}
 
 

 
### deregister
> **DELETE** /monitoring/v1/data-source/{data_source_id}
>

> Deregisters and deletes a specific DataSource. You must specify the `data_source_id` of the DataSource to deregister.

| Type | Message |
| :--- | :--- |
| Request | [DataSourceRequest](data-source.md#datasourcerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text

```
{% endtab %}

{% tab title="Response Example" %}
```text

```
{% endtab %}
{% endtabs %}
 
 

 
### update_plugin
> **PUT** /monitoring/v1/data-source/{data_source_id}/plugin
>

> Updates the plugin of a specific DataSource. This method resets the plugin data in the DataSource to update the `metadata`.

| Type | Message |
| :--- | :--- |
| Request | [UpdateDataSourcePluginRequest](data-source.md#updatedatasourcepluginrequest) |
| Response |  [DataSourceInfo](data-source.md#datasourceinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text

```
{% endtab %}

{% tab title="Response Example" %}
```text

```
{% endtab %}
{% endtabs %}
 
 

 
### verify_plugin
> **PUT** /monitoring/v1/data-source/{data_source_id}/plugin/verify
>

> Verifies the plugin of a specific DataSource. This method validates the plugin data, `version` and `endpoint`.

| Type | Message |
| :--- | :--- |
| Request | [DataSourceRequest](data-source.md#datasourcerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text

```
{% endtab %}

{% tab title="Response Example" %}
```text

```
{% endtab %}
{% endtabs %}
 
 

 
### get
> **GET** /monitoring/v1/data-source/{data_source_id}
>

> Gets a specific DataSource. Prints detailed information about the DataSource, including `name`, `state`, and `plugin_info`.

| Type | Message |
| :--- | :--- |
| Request | [GetDataSourceRequest](data-source.md#getdatasourcerequest) |
| Response |  [DataSourceInfo](data-source.md#datasourceinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text

```
{% endtab %}

{% tab title="Response Example" %}
```text

```
{% endtab %}
{% endtabs %}
 
 

 
### list
> **GET** /monitoring/v1/data-sources
>
> **POST** /monitoring/v1/data-sources/search


> Gets a list of all DataSources. You can use a query to get a filtered list of DataSources.

| Type | Message |
| :--- | :--- |
| Request | [DataSourceQuery](data-source.md#datasourcequery) |
| Response |  [DataSourcesInfo](data-source.md#datasourcesinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text

```
{% endtab %}

{% tab title="Response Example" %}
```text

```
{% endtab %}
{% endtabs %}
 
 

 
### stat
> **POST** /monitoring/v1/data-sources/stat
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
