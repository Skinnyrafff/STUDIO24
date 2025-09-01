import React from 'react';
import { FaPlus, FaTrash } from 'react-icons/fa';
import './Calendar.css';

// Función para generar las horas del día
const generateTimeSlots = () => {
  const slots = [];
  for (let i = 9; i <= 20; i++) {
    slots.push(`${i.toString().padStart(2, '0')}:00`);
  }
  return slots;
};

const daysOfWeek = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'];
const timeSlots = generateTimeSlots();

// Datos de ejemplo de citas (más adelante vendrán de la API)
// Formato: 'YYYY-MM-DDTHH:MM:SS'
const bookedAppointments = {
  'Lunes-10:00': true,
  'Miércoles-13:00': true,
  'Viernes-15:00': true,
  'Sábado-11:00': true,
};


const Calendar = () => {
  return (
    <div className="calendar-container">
      <div className="calendar-header">
        <div className="time-column-header">Hora</div>
        {daysOfWeek.map(day => (
          <div key={day} className="day-header">{day}</div>
        ))}
      </div>
      <div className="calendar-body">
        <div className="time-column">
          {timeSlots.map(time => (
            <div key={time} className="time-label">{time}</div>
          ))}
        </div>
        <div className="schedule-grid">
          {daysOfWeek.map(day => (
            <div key={day} className="day-column">
              {timeSlots.map(time => {
                const isBooked = !!bookedAppointments[`${day}-${time}`];
                return (
                  <div
                    key={`${day}-${time}`}
                    className={`grid-cell ${isBooked ? 'booked' : 'available'}`}
                  >
                    <div className="cell-actions">
                      {isBooked ? (
                        <button className="action-btn delete-btn"><FaTrash /></button>
                      ) : (
                        <button className="action-btn add-btn"><FaPlus /></button>
                      )}
                    </div>
                  </div>
                );
              })}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Calendar;