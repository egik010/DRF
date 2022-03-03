import React from 'react'
import logo from './logo.svg';
import './App.css';
import UserList from './components/UserList';
import Menu from './components/Menu';
import Footer from './components/Footer';

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [
                {
                    "username": "admin1",
                    "first_name": "Админ1",
                    "last_name": "Петрович",
                    "email": "admin@mail.ru"
                },
                {
                    "username": "manager1",
                    "first_name": "Менеджер1",
                    "last_name": "Васильевич",
                    "email": "manager1@mail.ru"
                },
                {
                    "username": "developer1",
                    "first_name": "Разработчик1",
                    "last_name": "Иванович",
                    "email": "developer1@mail.ru"
                },
                {
                    "username": "admin",
                    "first_name": "",
                    "last_name": "",
                    "email": "admin0@mail.ru"
                }
            ]
        }
    }

    render() {
        return (
            <div>
                <UserList users={this.state.users} />
            </div>
        )
    }

}

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

export default App;
