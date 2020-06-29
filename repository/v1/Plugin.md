---
description:  
---
# Plugin

>  **Package : spaceone.api.repository.v1**

## Plugin

{% hint style="info" %}
**Plugin Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [register](Plugin.md#register)| [CreatePluginRequest](Plugin.md#createpluginrequest) | [PluginInfo](Plugin.md#plugininfo) |  |
| 2 | [update](Plugin.md#update)| [UpdatePluginRequest](Plugin.md#updatepluginrequest) | [PluginInfo](Plugin.md#plugininfo) |  |
| 3 | [deregister](Plugin.md#deregister)| [PluginRequest](Plugin.md#pluginrequest) |[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 4 | [enable](Plugin.md#enable)| [PluginRequest](Plugin.md#pluginrequest) | [PluginInfo](Plugin.md#plugininfo) |  |
| 5 | [disable](Plugin.md#disable)| [PluginRequest](Plugin.md#pluginrequest) | [PluginInfo](Plugin.md#plugininfo) |  |
| 6 | [get_versions](Plugin.md#get_versions)| [RepositoryPluginRequest](Plugin.md#repositorypluginrequest) | [VersionsInfo](Plugin.md#versionsinfo) |  |
| 7 | [get](Plugin.md#get)| [GetRepositoryPluginRequest](Plugin.md#getrepositorypluginrequest) | [PluginInfo](Plugin.md#plugininfo) |  |
| 8 | [list](Plugin.md#list)| [PluginQuery](Plugin.md#pluginquery) | [PluginsInfo](Plugin.md#pluginsinfo) |  |
| 9 | [stat](Plugin.md#stat)| [PluginStatQuery](Plugin.md#pluginstatquery) |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |

### register
> **POST** /repository/v1/plugins
>



| Type | Message |
| :--- | :--- |
| Request | [CreatePluginRequest](Plugin.md#createpluginrequest) |
| Response |  [PluginInfo](Plugin.md#plugininfo)  |



### update
> **PUT** /repository/v1/plugin/{plugin_id}
>



| Type | Message |
| :--- | :--- |
| Request | [UpdatePluginRequest](Plugin.md#updatepluginrequest) |
| Response |  [PluginInfo](Plugin.md#plugininfo)  |



### deregister
> **DELETE** /repository/v1/plugin/{plugin_id}
>



| Type | Message |
| :--- | :--- |
| Request | [PluginRequest](Plugin.md#pluginrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |



### enable
> **PUT** /repository/v1/plugin/{plugin_id}/enable
>



| Type | Message |
| :--- | :--- |
| Request | [PluginRequest](Plugin.md#pluginrequest) |
| Response |  [PluginInfo](Plugin.md#plugininfo)  |



### disable
> **PUT** /repository/v1/plugin/{plugin_id}/disable
>



| Type | Message |
| :--- | :--- |
| Request | [PluginRequest](Plugin.md#pluginrequest) |
| Response |  [PluginInfo](Plugin.md#plugininfo)  |



### get_versions
> **GET** /repository/v1/plugins/{plugin_id}/versions
>



| Type | Message |
| :--- | :--- |
| Request | [RepositoryPluginRequest](Plugin.md#repositorypluginrequest) |
| Response |  [VersionsInfo](Plugin.md#versionsinfo)  |



### get
> **GET** /repository/v1/plugins/{plugin_id}
>



| Type | Message |
| :--- | :--- |
| Request | [GetRepositoryPluginRequest](Plugin.md#getrepositorypluginrequest) |
| Response |  [PluginInfo](Plugin.md#plugininfo)  |



### list
> **GET** /repository/v1/plugins
>
> **POST** /repository/v1/plugins/search




| Type | Message |
| :--- | :--- |
| Request | [PluginQuery](Plugin.md#pluginquery) |
| Response |  [PluginsInfo](Plugin.md#pluginsinfo)  |



### stat
> **POST** /repository/v1/plugins/stat
>



| Type | Message |
| :--- | :--- |
| Request | [PluginStatQuery](Plugin.md#pluginstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |





## Message

### CreatePluginRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string |✅ ||
| 2 | service_type |string |✅ ||
| 3 | image |string |✅ ||
| 4 | provider |string |❌ ||
| 5 | capability |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 6 | template |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 7 | labels |string |❌ ||
| 8 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 9 | project_id |string |❌ ||
| 10 | domain_id |string |✅ ||

### GetRepositoryPluginRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | plugin_id |string |✅ ||
| 2 | domain_id |string |✅ ||
| 3 | repository_id |string |❌ ||
| 4 | only |string |❌ ||

### PluginInfo
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
      <td style="text-align:left">plugin_id</td>
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
      <td style="text-align:left">image</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">registry_url</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left">
<p>PluginInfo.State</p>
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
      <td style="text-align:left">6</td>
      <td style="text-align:left">service_type</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">provider</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">capability</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">template</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">labels</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">11</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">12</td>
      <td style="text-align:left">repository_info</td>
      <td style="text-align:left">
<a href="Plugin.md#repositoryinfo">RepositoryInfo</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">13</td>
      <td style="text-align:left">project_id</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">14</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">15</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
  </tbody>
</table>


### PluginQuery
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
      <td style="text-align:left">plugin_id</td>
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
<p>PluginQuery.State</p>
        <ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
        </ul>
</td><td style="text-align:left">❌</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">service_type</td>
      <td style="text-align:left">

string

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
      <td style="text-align:left">repository_id</td>
      <td style="text-align:left">

string

</td><td style="text-align:left">✅</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">

string

</td><td style="text-align:left">✅</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
  </tbody>
</table>


### PluginRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | plugin_id |string |✅ ||
| 2 | domain_id |string |✅ ||

### PluginStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) |✅ ||
| 2 | repository_id |string |✅ ||
| 3 | domain_id |string |✅ ||

### PluginsInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results |[PluginInfo](Plugin.md#plugininfo) | ||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||

### RepositoryPluginRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | plugin_id |string |✅ ||
| 2 | domain_id |string |✅ ||
| 3 | repository_id |string |❌ ||

### UpdatePluginRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | plugin_id |string |✅ ||
| 2 | name |string |❌ ||
| 3 | capability |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 4 | template |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 5 | labels |string |❌ ||
| 6 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |❌ ||
| 7 | domain_id |string |✅ ||

### VersionsInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | version |string | |Deprecated|
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||
| 3 | results |string | ||
