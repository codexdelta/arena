import React, { useState } from 'react';

import './App.css';


type TodoProps = {
  title: string,
  description: string
}

const TodoComponent = ({ title, description }: TodoProps) => <li>
  {`${title} : ${description}`}
</li>


const AddNewTodo = () => {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');

  return (
    <div className="newTodo">
      <input type="text" placeholder="title" value={title} onChange={(event: { target: { value: React.SetStateAction<string>; }; }) => setTitle(event.target.value)} />
      <input type="text" placeholder="description" value={description} onChange={(event: { target: { value: React.SetStateAction<string>; }; }) => setDescription(event.target.value)} />
      <button>Add</button>
    </div>
  )
}

function App() {
  const data = [{ id: 1, title: 'viva', description: 'vida' }, { id: 2, title: 'tiva', description: 'piva' }]


  return (
    <div className="App">
      <AddNewTodo />
      <div>
        <ul>
          {
            data.map(val => {
              return (
                <TodoComponent key={val.id} {...val} />
              )
            })
          }
        </ul>
      </div>

    </div>
  );
}

export default App;
