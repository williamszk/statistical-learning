function ListOfTodo() {
	const myTodoList = ["Do the dishes", "Make a bread", "Study React"];

	return (
		<ul>
			{myTodoList.map((item) => (
				<li key={item}> {item} </li>
			))}
		</ul>
	);
}

export default ListOfTodo;
