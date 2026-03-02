/* **************************************************************************
 * PROJECT: VITALIS-PRIME - THE CONVERGENT INTELLIGENCE KERNEL
 * AUTHOR: JORGE HUMBERTO DAVALOS GONZALEZ (CEO & FOUNDER)
 * ORGANIZATION: ORZWORKNET FOUNDATION
 * LOCATION: GUADALAJARA, JALISCO, MEXICO
 * LICENSE: MIT (2026) | CONTACT: luckystrike@gmail.com
 * ************************************************************************** */

const io = require('socket.io')(process.env.PORT || 3000, {
  cors: {
    origin: "*", // Configuración para el Dashboard de neón cyan
    methods: ["GET", "POST"]
  }
});

/**
 * Canal de Comunicación Crítico: Orion Core -> Aurelius-Omni
 */
io.on('connection', (socket) => {
  console.log('>>> VITALIS-PRIME: Link Established with Command Bridge');

  // Protocolo de Reporte de Autocuración (Self-Healing)
  socket.on('ORION_CORE_ALERT', (data) => {
    const enrichedAlert = {
      ...data,
      timestamp: new Date().toISOString(),
      supervisor: "Aurelius-Omni",
      verified_by: "Jorge Humberto Davalos Gonzalez", //
      organization: "ORZWORKNET Foundation" //
    };

    // Retransmitir a la interfaz visual (Command Bridge)
    socket.broadcast.emit('BRIDGE_UPDATE', enrichedAlert);
    
    console.log(`[ALERT] Self-Healing Active: ${data.action}`);
  });

  socket.on('disconnect', () => {
    console.log('<<< VITALIS-PRIME: Link Terminated');
  });
});

module.exports = io;

