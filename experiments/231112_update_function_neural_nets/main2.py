from helper2 import (
    InputDesc,
    HiddenLayerDesc,
    TrainingData,
    TrainingDataRecord,
    create_intermediate_results,
)


def main():
    input_desc = InputDesc(
        input_layer=2,
        output_layer=1,
        hidden_layers=[HiddenLayerDesc(position=1, number_nodes=3)],
    )
    # Why do I need 3 nodes, instead of 2 or 4?
    training_data = TrainingData(
        content=[
            TrainingDataRecord(inputs=[0, 0], outputs=[0]),
            TrainingDataRecord(inputs=[1, 0], outputs=[1]),
            TrainingDataRecord(inputs=[0, 1], outputs=[1]),
            TrainingDataRecord(inputs=[0, 0], outputs=[0]),
        ]
    )

    print(create_intermediate_results(input_desc, training_data))


if __name__ == "__main__":
    main()
