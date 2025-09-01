import React, { useState, useEffect } from 'react';
import axios from 'axios';

const UserList = () => {
  const [users, setUsers] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/users');
        setUsers(response.data);
      } catch (err) {
        setError('Error al obtener los usuarios del backend.');
        console.error(err);
      }
    };

    fetchUsers();
  }, []); // El array vacío significa que este efecto se ejecuta una vez al montar el componente

  if (error) {
    return <div>{error}</div>;
  }

  return (
    <div>
      <h1>Lista de Usuarios</h1>
      <ul>
        {users.map(user => (
          <li key={user.id}>{user.name} - {user.email}</li> // Asumiendo que el usuario tiene id, name y email
        ))}
      </ul>
    </div>
  );
};

export default UserList;