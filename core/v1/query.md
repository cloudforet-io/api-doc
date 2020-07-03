---
description: null
---

# Query

> **Package : spaceone.api.core.v1**

## Message

### AggregateCount

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name | string |  |  |

### AggregateGroup

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | keys | [AggregateGroupKey](query.md#aggregategroupkey) |  |  |
| 2 | fields | [AggregateGroupField](query.md#aggregategroupfield) |  |  |

### AggregateGroupField

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | key | string |  |  |
| 2 | k | string |  |  |
| 3 | name | string |  |  |
| 4 | n | string |  |  |
| 5 | operator | string |  |  |
| 6 | o | string |  |  |

### AggregateGroupKey

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | key | string |  |  |
| 2 | k | string |  |  |
| 3 | name | string |  |  |
| 4 | n | string |  |  |

### AggregateUnwind

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | path | string |  |  |

### Filter

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | key | string |  |  |
| 2 | k | string |  |  |
| 3 | value | [google.protobuf.Value](https://developers.google.com/protocol-buffers/docs/reference/overview) |  |  |
| 4 | v | [google.protobuf.Value](https://developers.google.com/protocol-buffers/docs/reference/overview) |  |  |
| 5 | operator | string |  |  |
| 6 | o | string |  |  |

### Page

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | start | [uint32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) |  |  |
| 2 | limit | [uint32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) |  |  |

### Query

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | filter | [Filter](query.md#filter) |  |  |
| 2 | filter\_or | [Filter](query.md#filter) |  |  |
| 3 | sort | [Sort](query.md#sort) |  |  |
| 4 | page | [Page](query.md#page) |  |  |
| 5 | minimal | bool |  |  |
| 6 | count\_only | bool |  |  |
| 7 | only | string |  |  |
| 8 | keyword | string |  |  |

### Sort

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | key | string |  |  |
| 2 | desc | bool |  |  |

### StatisticsAggregate

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | unwind | [AggregateUnwind](query.md#aggregateunwind) |  |  |
| 2 | group | [AggregateGroup](query.md#aggregategroup) |  |  |
| 3 | count | [AggregateCount](query.md#aggregatecount) |  |  |

### StatisticsQuery

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | filter | [Filter](query.md#filter) |  |  |
| 2 | filter\_or | [Filter](query.md#filter) |  |  |
| 3 | aggregate | [StatisticsAggregate](query.md#statisticsaggregate) |  |  |
| 4 | sort | [StatisticsSort](query.md#statisticssort) |  |  |
| 5 | page | [Page](query.md#page) |  |  |
| 6 | limit | [uint32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) |  |  |

### StatisticsSort

| No | Field | Type | Required | Description |
| :--- | :--- | :--- | :--- | :--- |
| 1 | name | string |  |  |
| 2 | desc | bool |  |  |

