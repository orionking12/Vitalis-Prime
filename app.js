/* **************************************************************************
 * PROJECT: VITALIS-PRIME - THE CONVERGENT INTELLIGENCE KERNEL
 * ARCHITECT: JORGE HUMBERTO DAVALOS GONZALEZ (CEO & FOUNDER)
 * ORGANIZATION: ORZWORKNET FOUNDATION
 * LOCATION: GUADALAJARA, JALISCO, MEXICO
 * LICENSE: MIT (2026) | CONTACT: luckystrike@gmail.com
 * ************************************************************************** */

require('dotenv').config();
const { spawn } = require('child_process');
const io = require('./src/network/socket');

console.log(`
  VITALIS-PRIME KERNEL v1.0
  -------------------------
  Autor: Jorge Humberto Davalos Gonzalez
  Status: Initializing Convergent Intelligence...
`);

/**
 * 1. Inicializar el Motor de Inteligencia Neuro-Híbrida (Python)
 * Este proceso arranca el Kernel que gestiona el Concept Drift.
 */
const pythonKernel = spawn('python', ['src/vitalis_kernel.py']);

pythonKernel.stdout.on('data', (data) => {
    console.log(`[PYTHON_KERNEL]: ${data}`);
    // Si el Kernel detecta un colapso, lo enviamos al Dashboard vía Sockets
    if (data.includes("CRITICAL_DRIFT")) {
        io.emit('ORION_CORE_ALERT', {
            action: "Emergency Self-Healing Protocol",
            intensity: 0.95,
            verified_by: process.env.AUTHOR_NAME
        });
    }
});

pythonKernel.stderr.on('data', (data) => {
    console.error(`[KERNEL_ERROR]: ${data}`);
});

/**
 * 2. Iniciar el Servidor de Supervisión (Aurelius-Omni)
 * Mantiene la conexión activa con el Command Bridge de neón cyan.
 */
const PORT = process.env.PORT || 3001;
console.log(`>>> VITALIS-PRIME Bridge active on port ${PORT}`);
console.log(`>>> Licensed to: ${process.env.AUTHOR_NAME}`);

// Exportar para uso del sistema
module.exports = { pythonKernel, io };
