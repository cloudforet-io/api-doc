---
description:  
---
# Query

>  **Package : spaceone.api.core.v1**

## 

## Message

### AggregateCount
| Field | Type |  Description |
| :--- | :--- | :--- |
| name |string | |

### AggregateGroup
| Field | Type |  Description |
| :--- | :--- | :--- |
| keys |[list of AggregateGroupKey](query.md#aggregategroupkey) | |
| fields |[list of AggregateGroupField](query.md#aggregategroupfield) | |

### AggregateGroupField
| Field | Type |  Description |
| :--- | :--- | :--- |
| key |string | |
| k |string | |
| name |string | |
| n |string | |
| operator |string | |
| o |string | |
| fields |[list of AggregateGroupSubField](query.md#aggregategroupsubfield) | |
| conditions |[list of AggregateSubCondition](query.md#aggregatesubcondition) | |

### AggregateGroupKey
| Field | Type |  Description |
| :--- | :--- | :--- |
| key |string | |
| k |string | |
| name |string | |
| n |string | |
| date_format |string | |

### AggregateGroupSubField
| Field | Type |  Description |
| :--- | :--- | :--- |
| key |string | |
| k |string | |
| name |string | |
| n |string | |

### AggregateProject
| Field | Type |  Description |
| :--- | :--- | :--- |
| fields |[list of AggregateProjectField](query.md#aggregateprojectfield) | |
| exclude_keys |bool | |

### AggregateProjectField
| Field | Type |  Description |
| :--- | :--- | :--- |
| key |string | |
| k |string | |
| name |string | |
| n |string | |
| operator |string | |
| o |string | |

### AggregateSort
| Field | Type |  Description |
| :--- | :--- | :--- |
| key |string | |
| desc |bool | |
| keys |[list of SortKey](query.md#sortkey) | |

### AggregateSubCondition
| Field | Type |  Description |
| :--- | :--- | :--- |
| key |string | |
| k |string | |
| value |[google.protobuf.Value](https://developers.google.com/protocol-buffers/docs/reference/overview) | |
| v |[google.protobuf.Value](https://developers.google.com/protocol-buffers/docs/reference/overview) | |
| operator |string | |
| o |string | |

### AggregateUnwind
| Field | Type |  Description |
| :--- | :--- | :--- |
| path |string | |

### Filter
| Field | Type |  Description |
| :--- | :--- | :--- |
| key |string | |
| k |string | |
| value |[google.protobuf.Value](https://developers.google.com/protocol-buffers/docs/reference/overview) | |
| v |[google.protobuf.Value](https://developers.google.com/protocol-buffers/docs/reference/overview) | |
| operator |string | |
| o |string | |

### Page
| Field | Type |  Description |
| :--- | :--- | :--- |
| start |[uint32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
| limit |[uint32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### Query
| Field | Type |  Description |
| :--- | :--- | :--- |
| filter |[list of Filter](query.md#filter) | |
| filter_or |[list of Filter](query.md#filter) | |
| sort |[Sort](query.md#sort) | |
| page |[Page](query.md#page) | |
| minimal |bool | |
| count_only |bool | |
| only |list of string | |
| keyword |string | |

### Sort
| Field | Type |  Description |
| :--- | :--- | :--- |
| key |string | |
| desc |bool | |
| keys |[list of SortKey](query.md#sortkey) | |

### SortKey
| Field | Type |  Description |
| :--- | :--- | :--- |
| key |string | |
| desc |bool | |

### StatisticsAggregate
| Field | Type |  Description |
| :--- | :--- | :--- |
| unwind |[AggregateUnwind](query.md#aggregateunwind) | |
| group |[AggregateGroup](query.md#aggregategroup) | |
| count |[AggregateCount](query.md#aggregatecount) | |
| sort |[AggregateSort](query.md#aggregatesort) | |
| project |[AggregateProject](query.md#aggregateproject) | |
| limit |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |
| skip |[int32](https://github.com/protocolbuffers/protobuf/blob/master/src/google/protobuf/type.proto) | |

### StatisticsQuery
| Field | Type |  Description |
| :--- | :--- | :--- |
| filter |[list of Filter](query.md#filter) | |
| filter_or |[list of Filter](query.md#filter) | |
| aggregate |[list of StatisticsAggregate](query.md#statisticsaggregate) | |
| page |[Page](query.md#page) | |
| distinct |string | |
| keyword |string | |
