---
description:  
---
# Supervisor

>  **Package : spaceone.api.plugin.v1**

## Supervisor

{% hint style="info" %}
**Supervisor Methods:**

{%  endhint %}


| NO |  Method | Request Type | Response Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | [publish](Supervisor.md#publish)| [PublishSupervisorRequest](Supervisor.md#publishsupervisorrequest) | [SupervisorInfo](Supervisor.md#supervisorinfo) |  |
| 2 | [register](Supervisor.md#register)| [RegisterSupervisorRequest](Supervisor.md#registersupervisorrequest) | [SupervisorInfo](Supervisor.md#supervisorinfo) |  |
| 3 | [update](Supervisor.md#update)| [RegisterSupervisorRequest](Supervisor.md#registersupervisorrequest) | [SupervisorInfo](Supervisor.md#supervisorinfo) |  |
| 4 | [deregister](Supervisor.md#deregister)| [SupervisorRequest](Supervisor.md#supervisorrequest) |[google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|  |
| 5 | [enable](Supervisor.md#enable)| [SupervisorRequest](Supervisor.md#supervisorrequest) | [SupervisorInfo](Supervisor.md#supervisorinfo) |  |
| 6 | [disable](Supervisor.md#disable)| [SupervisorRequest](Supervisor.md#supervisorrequest) | [SupervisorInfo](Supervisor.md#supervisorinfo) |  |
| 7 | [recover_plugin](Supervisor.md#recover_plugin)| [RecoverPluginRequest](Supervisor.md#recoverpluginrequest) | [PluginInfo](Supervisor.md#plugininfo) |  |
| 8 | [get](Supervisor.md#get)| [GetSupervisorRequest](Supervisor.md#getsupervisorrequest) | [SupervisorInfo](Supervisor.md#supervisorinfo) |  |
| 9 | [list](Supervisor.md#list)| [SupervisorQuery](Supervisor.md#supervisorquery) | [SupervisorsInfo](Supervisor.md#supervisorsinfo) |  |
| 10 | [stat](Supervisor.md#stat)| [SupervisorStatQuery](Supervisor.md#supervisorstatquery) |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|  |
| 11 | [list_plugins](Supervisor.md#list_plugins)| [PluginQuery](Supervisor.md#pluginquery) | [PluginsInfo](Supervisor.md#pluginsinfo) |  |

### publish
> **POST** /plugin/v1/supervisors
>



| Type | Message |
| :--- | :--- |
| Request | [PublishSupervisorRequest](Supervisor.md#publishsupervisorrequest) |
| Response |  [SupervisorInfo](Supervisor.md#supervisorinfo)  |



### register
> **POST** /plugin/v1/supervisor/{supervisor_id}/register
>



| Type | Message |
| :--- | :--- |
| Request | [RegisterSupervisorRequest](Supervisor.md#registersupervisorrequest) |
| Response |  [SupervisorInfo](Supervisor.md#supervisorinfo)  |



### update
> **PUT** /plugin/v1/supervisor/{supervisor_id}
>



| Type | Message |
| :--- | :--- |
| Request | [RegisterSupervisorRequest](Supervisor.md#registersupervisorrequest) |
| Response |  [SupervisorInfo](Supervisor.md#supervisorinfo)  |



### deregister
> **DELETE** /plugin/v1/supervisor/{supervisor_id}/register
>



| Type | Message |
| :--- | :--- |
| Request | [SupervisorRequest](Supervisor.md#supervisorrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |



### enable
> **PUT** /plugin/v1/supervisor/{supervisor_id}/enable
>



| Type | Message |
| :--- | :--- |
| Request | [SupervisorRequest](Supervisor.md#supervisorrequest) |
| Response |  [SupervisorInfo](Supervisor.md#supervisorinfo)  |



### disable
> **PUT** /plugin/v1/supervisor/{supervisor_id}/disable
>



| Type | Message |
| :--- | :--- |
| Request | [SupervisorRequest](Supervisor.md#supervisorrequest) |
| Response |  [SupervisorInfo](Supervisor.md#supervisorinfo)  |



### recover_plugin
> **POST** /plugin/v1/supervisor/{supervisor_id}/plugin/{plugin_id}/recover
>



| Type | Message |
| :--- | :--- |
| Request | [RecoverPluginRequest](Supervisor.md#recoverpluginrequest) |
| Response |  [PluginInfo](Supervisor.md#plugininfo)  |



### get
> **GET** /plugin/v1/supervisor/{supervisor_id}
>



| Type | Message |
| :--- | :--- |
| Request | [GetSupervisorRequest](Supervisor.md#getsupervisorrequest) |
| Response |  [SupervisorInfo](Supervisor.md#supervisorinfo)  |



### list
> **GET** /plugin/v1/supervisors
>
> **POST** /plugin/v1/supervisors/search




| Type | Message |
| :--- | :--- |
| Request | [SupervisorQuery](Supervisor.md#supervisorquery) |
| Response |  [SupervisorsInfo](Supervisor.md#supervisorsinfo)  |



### stat
> **POST** /plugin/v1/supervisors/stat
>



| Type | Message |
| :--- | :--- |
| Request | [SupervisorStatQuery](Supervisor.md#supervisorstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |



### list_plugins
> **GET** /plugin/v1/supervisor/{supervisor_id}/plugins
>
> **POST** /plugin/v1/supervisor/{supervisor_id}/plugins/search




| Type | Message |
| :--- | :--- |
| Request | [PluginQuery](Supervisor.md#pluginquery) |
| Response |  [PluginsInfo](Supervisor.md#pluginsinfo)  |





## Message

### GetSupervisorRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | supervisor_id |string | |required|
| 2 | domain_id |string | |required|
| 3 | only |string | |optional|

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
      <td style="text-align:left">version</td>
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
<p>PluginInfo.State</p>
        <ul>
          	<li>NONE</li>
          	<li>PROVISIONING</li>
          	<li>ACTIVE</li>
          	<li>RE_PROVISIONING</li>
          	<li>ERROR</li>
        </ul>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">endpoint</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">supervisor_id</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">supervisor_name</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">managed</td>
      <td style="text-align:left">

bool

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">endpoints</td>
      <td style="text-align:left">

string

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
      <td style="text-align:left">supervisor_id</td>
      <td style="text-align:left">

string

</td><td style="text-align:left">❌</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
    <tr>
      <td style="text-align:left">3</td>
      <td style="text-align:left">hostname</td>
      <td style="text-align:left">

string

</td><td style="text-align:left">❌</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">plugin_id</td>
      <td style="text-align:left">

string

</td><td style="text-align:left">❌</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">version</td>
      <td style="text-align:left">

string

</td><td style="text-align:left">❌</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left">
<p>PluginQuery.State</p>
        <ul>
          	<li>NONE</li>
          	<li>PROVISIONING</li>
          	<li>ACTIVE</li>
          	<li>RE_PROVISIONING</li>
          	<li>ERROR</li>
        </ul>
</td><td style="text-align:left">❌</td>
<td style="text-align:left"></td>
        <td style="text-align:left"></td>

    </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">endpoint</td>
      <td style="text-align:left">

string

</td><td style="text-align:left">❌</td>
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


### PluginsInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results |[PluginInfo](Supervisor.md#plugininfo) | ||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||

### PublishSupervisorRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name |string | |required|
| 2 | hostname |string | |required|
| 3 | secret_key |string | |optional|
| 4 | plugin_info |[PluginInfo](Supervisor.md#plugininfo) | |optional|
| 5 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |optional|
| 6 | is_public |bool | |optional|
| 7 | domain_id |string | |required|

### RecoverPluginRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | supervisor_id |string | |required|
| 2 | plugin_id |string | |required|
| 3 | version |string | |required|
| 4 | domain_id |string | |required|

### RegisterSupervisorRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | supervisor_id |string | |required|
| 2 | name |string | |required|
| 3 | is_public |bool | |optional|
| 4 | priority |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |optional|
| 5 | labels |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |optional|
| 6 | tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) | |optional|
| 7 | domain_id |string | |required|

### SupervisorInfo
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
      <td style="text-align:left">supervisor_id</td>
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
      <td style="text-align:left">hostname</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">4</td>
      <td style="text-align:left">state</td>
      <td style="text-align:left">
<p>SupervisorInfo.State</p>
        <ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
          	<li>PENDING</li>
          	<li>DISCONNECTED</li>
        </ul>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">5</td>
      <td style="text-align:left">is_public</td>
      <td style="text-align:left">

bool

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">6</td>
      <td style="text-align:left">domain_id</td>
      <td style="text-align:left">

string

</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">7</td>
      <td style="text-align:left">tags</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">8</td>
      <td style="text-align:left">labels</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">9</td>
      <td style="text-align:left">created_at</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left">10</td>
      <td style="text-align:left">updated_at</td>
      <td style="text-align:left">
<a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/timestamp.proto">google.protobuf.Timestamp</a>
</td>
        <td style="text-align:left"></td>
<td style="text-align:left"></td>
    </tr>
  </tbody>
</table>


### SupervisorQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query) |❌ ||
| 2 | supervisor_id |string |❌ ||
| 3 | name |string |❌ ||
| 4 | is_public |bool |❌ ||
| 5 | domain_id |string |✅ ||

### SupervisorRequest
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | supervisor_id |string | |required|
| 2 | domain_id |string | |required|

### SupervisorStatQuery
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query) |✅ ||
| 2 | domain_id |string |✅ ||

### SupervisorsInfo
| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | results |[SupervisorInfo](Supervisor.md#supervisorinfo) | ||
| 2 | total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | ||
