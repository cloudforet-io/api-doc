---
description:  
---
# Data source

>  **Package : spaceone.api.monitoring.v1**

## DataSource

{% hint style="info" %}
**DataSource Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [register](Data-source.md#register)| [RegisterDataSourceRequest](Data-source.md#registerdatasourcerequest) | [DataSourceInfo](Data-source.md#datasourceinfo) |  |
| 2 | [update](Data-source.md#update)| [UpdateDataSourceRequest](Data-source.md#updatedatasourcerequest) | [DataSourceInfo](Data-source.md#datasourceinfo) |  |
| 3 | [enable](Data-source.md#enable)| [DataSourceRequest](Data-source.md#datasourcerequest) | [DataSourceInfo](Data-source.md#datasourceinfo) |  |
| 4 | [disable](Data-source.md#disable)| [DataSourceRequest](Data-source.md#datasourcerequest) | [DataSourceInfo](Data-source.md#datasourceinfo) |  |
| 5 | [deregister](Data-source.md#deregister)| [DataSourceRequest](Data-source.md#datasourcerequest) |[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 6 | [verify_plugin](Data-source.md#verify_plugin)| [DataSourceRequest](Data-source.md#datasourcerequest) | [VerifyInfo](Data-source.md#verifyinfo) |  |
| 7 | [get](Data-source.md#get)| [GetDataSourceRequest](Data-source.md#getdatasourcerequest) | [DataSourceInfo](Data-source.md#datasourceinfo) |  |
| 8 | [list](Data-source.md#list)| [DataSourceQuery](Data-source.md#datasourcequery) | [DataSourcesInfo](Data-source.md#datasourcesinfo) |  |
| 9 | [stat](Data-source.md#stat)| [DataSourceStatQuery](Data-source.md#datasourcestatquery) |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |

### register
> **POST** /monitoring/v1/data-sources
>



| Type | Message |
| :--- | :--- |
| Request | [RegisterDataSourceRequest](Data-source.md#registerdatasourcerequest) |
| Response |  [DataSourceInfo](Data-source.md#datasourceinfo)  |



### update
> **PUT** /monitoring/v1/data-source/{data_source_id}
>



| Type | Message |
| :--- | :--- |
| Request | [UpdateDataSourceRequest](Data-source.md#updatedatasourcerequest) |
| Response |  [DataSourceInfo](Data-source.md#datasourceinfo)  |



### enable
> **PUT** /monitoring/v1/data-source/{data_source_id}/enable
>



| Type | Message |
| :--- | :--- |
| Request | [DataSourceRequest](Data-source.md#datasourcerequest) |
| Response |  [DataSourceInfo](Data-source.md#datasourceinfo)  |



### disable
> **PUT** /monitoring/v1/data-source/{data_source_id}/disable
>



| Type | Message |
| :--- | :--- |
| Request | [DataSourceRequest](Data-source.md#datasourcerequest) |
| Response |  [DataSourceInfo](Data-source.md#datasourceinfo)  |



### deregister
> **DELETE** /monitoring/v1/data-source/{data_source_id}
>



| Type | Message |
| :--- | :--- |
| Request | [DataSourceRequest](Data-source.md#datasourcerequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |



### verify_plugin
> **PUT** /monitoring/v1/data-source/{data_source_id}/plugin/verify
>



| Type | Message |
| :--- | :--- |
| Request | [DataSourceRequest](Data-source.md#datasourcerequest) |
| Response |  [VerifyInfo](Data-source.md#verifyinfo)  |



### get
> **GET** /monitoring/v1/data-source/{data_source_id}
>



| Type | Message |
| :--- | :--- |
| Request | [GetDataSourceRequest](Data-source.md#getdatasourcerequest) |
| Response |  [DataSourceInfo](Data-source.md#datasourceinfo)  |



### list
> **GET** /monitoring/v1/data-sources
>
> **POST** /monitoring/v1/data-sources/search




| Type | Message |
| :--- | :--- |
| Request | [DataSourceQuery](Data-source.md#datasourcequery) |
| Response |  [DataSourcesInfo](Data-source.md#datasourcesinfo)  |



### stat
> **POST** /monitoring/v1/data-sources/stat
>



| Type | Message |
| :--- | :--- |
| Request | [DataSourceStatQuery](Data-source.md#datasourcestatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |





## Message

### DataSourceInfo
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">data_source_id</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left">
<p>DataSourceInfo.State</p>
        <ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">monitoring_type</td>
      <td style="text-align:left">
<p>MonitoringType</p>
        <ul>
          	<li>NONE</li>
          	<li>METRIC</li>
          	<li>LOG</li>
        </ul>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">provider</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">capability</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">plugin_info</td>
      <td style="text-align:left">
<a href="Data-source.md#plugininfo">PluginInfo</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
  </tbody>
</table>


### DataSourceQuery
<table>
  <thead>
    <tr>
      <th style="text-align:left">No</th>
      <th style="text-align:left">Field</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Required</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">1</td>
      <td style="text-align:left">query</td>
      <td style="text-align:left">
<a href="https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query">spaceone.api.core.v1.Query</a>
</td><td style="text-align:left">❌</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
    <tr>
      <td style="text-align:left">2</td>
      <td style="text-align:left">data_source_id</td>
      <td style="text-align:left">

string

</td><td style="text-align:left">❌</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">name</td>
      <td style="text-align:left">

string

</td><td style="text-align:left">❌</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left">

string

</td><td style="text-align:left">❌</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">monitoring_type</td>
      <td style="text-align:left">
<p>MonitoringType</p>
        <ul>
          	<li>NONE</li>
          	<li>METRIC</li>
          	<li>LOG</li>
        </ul>
</td><td style="text-align:left">❌</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">provider</td>
      <td style="text-align:left">

string

</td><td style="text-align:left">❌</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">

string

</td><td style="text-align:left">✅</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
  </tbody>
</table>


### DataSourceRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | data_source_id |string |✅ ||
| 2 | domain_id |string |✅ ||

### DataSourceStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) |✅ ||
| 2 | domain_id |string |✅ ||

### DataSourcesInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results |[DataSourceInfo](Data-source.md#datasourceinfo) | ||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||

### GetDataSourceRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | data_source_id |string |✅ ||
| 2 | domain_id |string |✅ ||
| 3 | only |string |❌ ||

### PluginInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | plugin_id |string | ||
| 2 | version |string | ||
| 3 | options |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | ||
| 4 | secret_id |string | ||
| 5 | provider |string | ||

### RegisterDataSourceRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string |✅ ||
| 2 | plugin_info |[PluginInfo](Data-source.md#plugininfo) |✅ ||
| 3 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 4 | domain_id |string |✅ ||

### UpdateDataSourceRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | data_source_id |string |✅ ||
| 2 | name |string |❌ ||
| 3 | plugin_info |[PluginInfo](Data-source.md#plugininfo) |❌ ||
| 4 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 5 | domain_id |string |✅ ||

### VerifyInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | status |bool | ||
