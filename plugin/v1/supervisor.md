---
description: A Supervisor is a resource managing the lifecycle of the plugin instances to deploy. A Supervisor manages the deployment of plugin instances by deploying or deleting the `pod` of the plugin instances.
---
# Supervisor

>  **Package : spaceone.api.plugin.v1**

## Supervisor

{% hint style="info" %}
**Supervisor Methods:**

{%  endhint %}


| Method | Request | Response |
| :----- | :-------- | :-------- |
| [**publish**](supervisor.md#publish)|   [PublishSupervisorRequest](supervisor.md#publishsupervisorrequest) |   [SupervisorInfo](supervisor.md#supervisorinfo) |
| [**register**](supervisor.md#register)|   [RegisterSupervisorRequest](supervisor.md#registersupervisorrequest) |   [SupervisorInfo](supervisor.md#supervisorinfo) |
| [**update**](supervisor.md#update)|   [RegisterSupervisorRequest](supervisor.md#registersupervisorrequest) |   [SupervisorInfo](supervisor.md#supervisorinfo) |
| [**deregister**](supervisor.md#deregister)|   [SupervisorRequest](supervisor.md#supervisorrequest) |  [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto)|
| [**enable**](supervisor.md#enable)|   [SupervisorRequest](supervisor.md#supervisorrequest) |   [SupervisorInfo](supervisor.md#supervisorinfo) |
| [**disable**](supervisor.md#disable)|   [SupervisorRequest](supervisor.md#supervisorrequest) |   [SupervisorInfo](supervisor.md#supervisorinfo) |
| [**recover_plugin**](supervisor.md#recover_plugin)|   [RecoverPluginRequest](supervisor.md#recoverpluginrequest) |   [PluginInfo](supervisor.md#plugininfo) |
| [**get**](supervisor.md#get)|   [GetSupervisorRequest](supervisor.md#getsupervisorrequest) |   [SupervisorInfo](supervisor.md#supervisorinfo) |
| [**list**](supervisor.md#list)|   [SupervisorQuery](supervisor.md#supervisorquery) |   [SupervisorsInfo](supervisor.md#supervisorsinfo) |
| [**stat**](supervisor.md#stat)|   [SupervisorStatQuery](supervisor.md#supervisorstatquery) |  [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|
| [**list_plugins**](supervisor.md#list_plugins)|   [PluginQuery](supervisor.md#pluginquery) |   [PluginsInfo](supervisor.md#pluginsinfo) | 
 

 
### publish
> **POST** /plugin/v1/supervisors
>

> Creates a new Supervisor. Only Users with the `MANAGED` permission can set the Supervisor `public`. The Supervisor manages the lifecycle of plugin instances by the Supervisor's state. When a Supervisor is created, the state of the resource is `PENDING`. If the state remains the same for 5 minutes, the state is changed to `DISCONNECTED`.

| Type | Message |
| :--- | :--- |
| Request | [PublishSupervisorRequest](supervisor.md#publishsupervisorrequest) |
| Response |  [SupervisorInfo](supervisor.md#supervisorinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "name": "test",
    "hostname": "dev-test2",
    "secret_key": "xxxxx",
    "tags": {
        "a": "b"
    }
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "supervisor_id": "supervisor-525982f2ae9a",
    "name": "test",
    "hostname": "dev-test2",
    "state": "ENABLED",
    "domain_id": "domain-1c5a6b8181ad",
    "tags": {
        "a": "b"
    },
    "labels": {},
    "created_at": "2022-01-15T05:42:02.999Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### register
> **POST** /plugin/v1/supervisor/{supervisor_id}/register
>

> Registers a specific Supervisor. You must specify the `supervisor_id` of the Supervisor to register. The `state` of the Supervisor changes from `PENDING` to `ENABLED`.

| Type | Message |
| :--- | :--- |
| Request | [RegisterSupervisorRequest](supervisor.md#registersupervisorrequest) |
| Response |  [SupervisorInfo](supervisor.md#supervisorinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{}
```
{% endtab %}
{% endtabs %}
 
 

 
### update
> **PUT** /plugin/v1/supervisor/{supervisor_id}
>

> Updates a specific Supervisor. You can make changes in Supervisor settings, including `labels`, `tags`, and the `bool` type parameter `is_public`.

| Type | Message |
| :--- | :--- |
| Request | [RegisterSupervisorRequest](supervisor.md#registersupervisorrequest) |
| Response |  [SupervisorInfo](supervisor.md#supervisorinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "supervisor_id": "supervisor-525982f2ae9a",
    "is_public": true,
    "priority": 10,
    "labels": {
        "a": "b"
    },
    "tags": {
        "c": "d"
    },
    "domain_id": "domain-1c5a6b8181ad"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "supervisor_id": "supervisor-525982f2ae9a",
    "name": "test",
    "hostname": "dev-test2",
    "state": "ENABLED",
    "is_public": true,
    "domain_id": "domain-1c5a6b8181ad",
    "tags": {
        "a": "b"
    },
    "labels": {
        "c": "d"
    },
    "created_at": "2022-06-15T05:42:02.999Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### deregister
> **DELETE** /plugin/v1/supervisor/{supervisor_id}/register
>

> Deregisters and deletes a specific Supervisor. You must specify the `supervisor_id` of the Supervisor to deregister.

| Type | Message |
| :--- | :--- |
| Request | [SupervisorRequest](supervisor.md#supervisorrequest) |
| Response | [google.protobuf.Empty](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/empty.proto) |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "supervisor_id": "supervisor-d73011256d55"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### enable
> **PUT** /plugin/v1/supervisor/{supervisor_id}/enable
>

> Enables a specific Supervisor. By changing the `state` parameter to `ENABLED`, the Supervisor can deploy or delete the `pod` of the plugin instance.

| Type | Message |
| :--- | :--- |
| Request | [SupervisorRequest](supervisor.md#supervisorrequest) |
| Response |  [SupervisorInfo](supervisor.md#supervisorinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "supervisor_id": "supervisor-d73011256d55"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "supervisor_id": "supervisor-d73011256d55",
    "name": "test-in-plugins",
    "hostname": "dev-test3",
    "state": "ENABLED",
    "domain_id": "domain-1c5a6b8181ad",
    "tags": {
        "a": "b"
    },
    "labels": {},
    "created_at": "2022-06-15T06:27:51.904Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### disable
> **PUT** /plugin/v1/supervisor/{supervisor_id}/disable
>

> Disables a specific Supervisor. By changing the `state` parameter to `DISABLED`, the Supervisor cannot deploy or delete the `pod` of the plugin instance.

| Type | Message |
| :--- | :--- |
| Request | [SupervisorRequest](supervisor.md#supervisorrequest) |
| Response |  [SupervisorInfo](supervisor.md#supervisorinfo)  |
{% tabs %}
{% tab title="Request Example" %}
```text
{
    "supervisor_id": "supervisor-d73011256d55"
}
```
{% endtab %}

{% tab title="Response Example" %}
```text
{
    "supervisor_id": "supervisor-d73011256d55",
    "name": "test-in-plugins",
    "hostname": "dev-test3",
    "state": "DISABLED",
    "domain_id": "domain-1c5a6b8181ad",
    "tags": {
        "a": "b"
    },
    "labels": {},
    "created_at": "2022-06-15T06:27:51.904Z"
}
```
{% endtab %}
{% endtabs %}
 
 

 
### recover_plugin
> **POST** /plugin/v1/supervisor/{supervisor_id}/plugin/{plugin_id}/recover
>


| Type | Message |
| :--- | :--- |
| Request | [RecoverPluginRequest](supervisor.md#recoverpluginrequest) |
| Response |  [PluginInfo](supervisor.md#plugininfo)  |
 
 

 
### get
> **GET** /plugin/v1/supervisor/{supervisor_id}
>


| Type | Message |
| :--- | :--- |
| Request | [GetSupervisorRequest](supervisor.md#getsupervisorrequest) |
| Response |  [SupervisorInfo](supervisor.md#supervisorinfo)  |
 
 

 
### list
> **GET** /plugin/v1/supervisors
>
> **POST** /plugin/v1/supervisors/search


> Gets a list of all Supervisors. You can use a query to get a filtered list of Supervisors.

| Type | Message |
| :--- | :--- |
| Request | [SupervisorQuery](supervisor.md#supervisorquery) |
| Response |  [SupervisorsInfo](supervisor.md#supervisorsinfo)  |
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
            "supervisor_id": "supervisor-3a091f899539",
            "name": "root",
            "hostname": "dev-supervisor.svc.cluster.local",
            "state": "ENABLED",
            "is_public": true,
            "domain_id": "domain-1c5a6b8181ad",
            "labels": {},
            "created_at": "2020-05-12T00:24:48.250Z"
        },
        {
            "supervisor_id": "supervisor-a4c287cba676",
            "name": "test",
            "hostname": "dev-test",
            "state": "ENABLED",
            "domain_id": "domain-1c5a6b8181ad",
            "tags": {
                "a": "b"
            },
            "labels": {},
            "created_at": "2022-06-15T05:39:15.886Z"
        }
    ],
    "total_count": 2
}
```
{% endtab %}
{% endtabs %}
 
 

 
### stat
> **POST** /plugin/v1/supervisors/stat
>


| Type | Message |
| :--- | :--- |
| Request | [SupervisorStatQuery](supervisor.md#supervisorstatquery) |
| Response | [google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto) |
 
 

 
### list_plugins
> **GET** /plugin/v1/supervisor/{supervisor_id}/plugins
>
> **POST** /plugin/v1/supervisor/{supervisor_id}/plugins/search


> Gets a list of all plugin instances regardless of Supervisors. Prints detailed information about the plugin instances, including `version`, `state`, and the relevant Supervisor.

| Type | Message |
| :--- | :--- |
| Request | [PluginQuery](supervisor.md#pluginquery) |
| Response |  [PluginsInfo](supervisor.md#pluginsinfo)  |
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
            "plugin_id": "plugin-openstack-inven-collector",
            "version": "0.4.1.20220609.122832",
            "state": "ACTIVE",
            "endpoint": "grpc://plugin-openstack-inven-collector-vbnnsoszfjsneiqz.dev-supervisor.svc.cluster.local:50051",
            "supervisor_id": "supervisor-3a091f899539",
            "supervisor_name": "root",
            "managed": true,
            "endpoints": [
                "grpc://172.16.16.234:50051"
            ]
        },
        {
            "plugin_id": "plugin-zabbix-mon-webhook",
            "version": "1.0",
            "state": "ACTIVE",
            "endpoint": "grpc://plugin-zabbix-mon-webhook-dgqqfqsqidieeuk.dev-supervisor.svc.cluster.local:50051",
            "supervisor_id": "supervisor-3a091f899539",
            "supervisor_name": "root",
            "managed": true,
            "endpoints": [
                "grpc://172.16.16.130:50051"
            ]
        }
    ],
    "total_count": 2
}
```
{% endtab %}
{% endtabs %}


## 

## Message

### GetSupervisorRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| supervisor_id |string|✔| |
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
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>PROVISIONING</li>
          	<li>ACTIVE</li>
          	<li>RE_PROVISIONING</li>
          	<li>ERROR</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">endpoint</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">supervisor_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">supervisor_name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">managed</td>
      <td style="text-align:left">bool</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">endpoints</td>
      <td style="text-align:left">list of string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### PluginQuery
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
      <td style="text-align:left; width:100px;">supervisor_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">hostname</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">plugin_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">version</td>
      <td style="text-align:left">string</td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>PROVISIONING</li>
          	<li>ACTIVE</li>
          	<li>RE_PROVISIONING</li>
          	<li>ERROR</li>
        </ul></td>
<td style="text-align:center">✘</td>
<td style="text-align:left"></td>
   </tr>
    <tr>
      <td style="text-align:left; width:100px;">endpoint</td>
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



### PluginsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of PluginInfo](supervisor.md#plugininfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### PublishSupervisorRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| name |string|✔| |
| hostname |string|✔| |
| secret_key |string|✘| |
| plugin_info |[list of PluginInfo](supervisor.md#plugininfo)|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| is_public |bool|✘| |
| domain_id |string|✔| |
| labels |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |

### RecoverPluginRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| supervisor_id |string|✔| |
| plugin_id |string|✔| |
| version |string|✔| |
| domain_id |string|✔| |

### RegisterSupervisorRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| supervisor_id |string|✔| |
| name |string|✘| |
| is_public |bool|✘| |
| priority |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto)|✘| |
| labels |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| tags |[google.protobuf.Struct](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto)|✘| |
| domain_id |string|✔| |

### SupervisorInfo
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
      <td style="text-align:left; width:100px;">supervisor_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">name</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">hostname</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">state</td>
      <td style="text-align:left"><ul>
          	<li>NONE</li>
          	<li>ENABLED</li>
          	<li>DISABLED</li>
          	<li>PENDING</li>
          	<li>DISCONNECTED</li>
        </ul></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">is_public</td>
      <td style="text-align:left">bool</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">domain_id</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">tags</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">labels</td>
      <td style="text-align:left"><a href="https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/struct.proto">google.protobuf.Struct</a></td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">created_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
    <tr>
      <td style="text-align:left; width:100px;">updated_at</td>
      <td style="text-align:left">string</td>
<td style="text-align:left"></td>

   </tr>
  </tbody>
</table>



### SupervisorQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.Query](https://spaceone-dev.gitbook.io/api-reference/common-v1/search-query)|✘| |
| supervisor_id |string|✘| |
| name |string|✘| |
| is_public |bool|✘| |
| domain_id |string|✔| |

### SupervisorRequest
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| supervisor_id |string|✔| |
| domain_id |string|✔| |

### SupervisorStatQuery
| Field | Type | Required | Description |
| :--- | :--- | :---: | :--- |
| query |[spaceone.api.core.v1.StatisticsQuery](https://spaceone-dev.gitbook.io/api-reference/common-v1/statistics-query)|✔| |
| domain_id |string|✔| |

### SupervisorsInfo
| Field | Type |  Description |
| :--- | :--- | :--- |
| results |[list of SupervisorInfo](supervisor.md#supervisorinfo) | |
| total_count |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
