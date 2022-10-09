import "./App.css";
import ListOfTodo from "./ListOfTodo";

function App() {
	return (
		<div className="App">
			<header className="App-header">
				<h1>Hello World!</h1>
				<p>This is a paragraph</p>
				<h2>My to-do list</h2>
				<ListOfTodo />
			</header>
		</div>
	);
}

export default App;
