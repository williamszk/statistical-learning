# TODO: make the below dict into a pydantic
# TODO: Make a generic way of creating the objects, given the number of
#       inputs, the number of nodes in each layer, the system should automatically
#       build the correct objects

from pydantic import BaseModel


class HiddenLayerDesc(BaseModel):
    position: int
    number_nodes: int


class InputDesc(BaseModel):
    input_layer: int
    hidden_layers: list[HiddenLayerDesc]
    output_layer: int


input_info = {
    "input_layer": 2,
    "hidden_layer_1": 3,
    "output_layer": 1,
}

# We can create a list of weights
# The list of weights can be created by the input_info that is given about
# the network
# Initially the values of the weights are given automatically


class Weight(BaseModel):
    weight_layer: int
    origin: int
    destination: int
    value: float
    epoch: int


def initialize_weights(input_desc: InputDesc):
    pass
    # this should return a WeightsHistory with just one epoch
    # the first with random values


class EpochHolder(BaseModel):
    epoch: int
    weights: list[Weight]


class WeightsHistory(BaseModel):
    content: list[EpochHolder]


# A matrix would be a better representation for this

weights = WeightsHistory(
    content=[
        EpochHolder(
            epoch=1,
            weights=[
                Weight(
                    epoch=1,
                    weight_layer=1,
                    origin=1,
                    destination=1,
                    value=-0.0424,
                ),
                Weight(
                    epoch=1,
                    weight_layer=1,
                    origin=1,
                    destination=2,
                    value=-0.740,
                ),
                Weight(
                    epoch=1,
                    weight_layer=1,
                    origin=1,
                    destination=3,
                    value=-0.961,
                ),
                Weight(
                    epoch=1,
                    weight_layer=1,
                    origin=2,
                    destination=1,
                    value=0.358,
                ),
                Weight(
                    epoch=1,
                    weight_layer=1,
                    origin=2,
                    destination=2,
                    value=-0.577,
                ),
                Weight(
                    epoch=1,
                    weight_layer=1,
                    origin=2,
                    destination=3,
                    value=-0.469,
                ),
                Weight(
                    epoch=1,
                    weight_layer=2,
                    origin=1,
                    destination=1,
                    value=-0.017,
                ),
                Weight(
                    epoch=1,
                    weight_layer=2,
                    origin=2,
                    destination=1,
                    value=-0.893,
                ),
                Weight(
                    epoch=1,
                    weight_layer=2,
                    origin=3,
                    destination=1,
                    value=0.148,
                ),
            ],
        )
    ]
)

# From the input info we should be able to create the below list


class NodesCarrier(BaseModel):
    inputs: list[float]
    hidden_layers: list[list[float]]
    output: list[float]


class StepNodeCarrier(BaseModel):
    step: int
    content: list[NodesCarrier]


class IntermediateResults(BaseModel):
    content: list[StepNodeCarrier]


class TrainingDataRecord(BaseModel):
    inputs: list[float]
    outputs: list[float]


class TrainingData(BaseModel):
    content: list[TrainingDataRecord]


def create_zeros_hidden_layer(input_desc: InputDesc) -> list[list[float]]:
    """We need some way to create value zeros to the hidden layer values."""
    hidden_layers = []
    for hidden_layer_desc in input_desc.hidden_layers:
        qtd_nodes = hidden_layer_desc.number_nodes
        zero_values = [0 for _ in range(qtd_nodes)]
        pos = hidden_layer_desc.position
        hidden_layers.insert(pos - 1, zero_values)
        # hidden_layer_desc.position is 1 for the 1st hidden layer
        # so we need to subtract 1
        # we use insert instead of append because the position is important
    return hidden_layers


def create_intermediate_results(
    input_desc: InputDesc, training_data: TrainingData
) -> IntermediateResults:
    # Maybe the "input_desc" does not match the "training_data"
    # We should check if they match

    content = []
    for training_data_record in training_data.content:
        input_data = training_data_record.inputs
        hidden_layers = create_zeros_hidden_layer(input_desc)
        node_carrier = NodesCarrier(
            inputs=input_data, hidden_layers=hidden_layers, output=[0]
        )
        content.append(node_carrier)

    intermediate_results = IntermediateResults(
        content=[StepNodeCarrier(step=1, content=content)]
    )
    return intermediate_results


# This should be created automatically
intermediate_results = [
    {
        "input01": 0,
        "input02": 0,
        "h1": None,
        "h2": None,
        "h3": None,
        "output": None,
        "step": 1,
    },
    {
        "input01": 1,
        "input02": 0,
        "h1": None,
        "h2": None,
        "h3": None,
        "output": None,
        "step": 1,
    },
    {
        "input01": 0,
        "input02": 1,
        "h1": None,
        "h2": None,
        "h3": None,
        "output": None,
        "step": 1,
    },
    {
        "input01": 1,
        "input02": 1,
        "h1": None,
        "h2": None,
        "h3": None,
        "output": None,
        "step": 1,
    },
]


def logit(x):
    e = 2.71828
    return 1 / (1 + e ** (-x))
