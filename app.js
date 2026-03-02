/* **************************************************************************
 * PROJECT: VITALIS-PRIME - THE CONVERGENT INTELLIGENCE KERNEL
 * ARCHITECT: JORGE HUMBERTO DAVALOS GONZALEZ (CEO & FOUNDER)
 * ORGANIZATION: ORZWORKNET FOUNDATION
 * LOCATION: GUADALAJARA, JALISCO, MEXICO
 * LICENSE: MIT (2026) | CONTACT: luckystrike@gmail.com
 * ************************************************************************** */

require('dotenv').config();
const { spawn } = require('child_process');
const path = require('path');
const io = require('./src/network/socket');

const AUTHOR = process.env.AUTHOR_NAME || "Jorge Humberto Davalos Gonzalez";
const PORT = process.env.PORT || 3001;

console.log(`
  VITALIS-PRIME KERNEL v2.0 (PRO)
  ------------------------------
  Autor: ${AUTHOR}
  Status: Initializing Convergent Intelligence...
`);

let pythonKernel;

function startKernel() {
    console.log(`[BRIDGE] Starting Python Kernel: src/kernel/servidor_nucleo.py`);

    pythonKernel = spawn('python', [path.join(__dirname, 'src/kernel/servidor_nucleo.py')]);

    pythonKernel.stdout.on('data', (data) => {
        const output = data.toString().trim();
        console.log(`[PYTHON_KERNEL]: ${output}`);

        // Critical Drift Detection
        if (output.includes("CRITICAL_DRIFT")) {
            console.warn(`[BRIDGE] !!! CRITICAL DRIFT ALERT !!!`);
            io.emit('ORION_CORE_ALERT', {
                action: "Emergency Self-Healing Protocol",
                intensity: 0.95,
                verified_by: AUTHOR,
                timestamp: new Date().toISOString()
            });
        }
    });

    pythonKernel.stderr.on('data', (data) => {
        console.error(`[KERNEL_ERROR]: ${data}`);
    });

    pythonKernel.on('close', (code) => {
        console.error(`[BRIDGE] Python Kernel exited with code ${code}. Restarting in 5s...`);
        setTimeout(startKernel, 5000);
    });
}

// Global Exception Handler
process.on('uncaughtException', (err) => {
    console.error(`[BRIDGE] Uncaught Exception: ${err.message}`);
});

startKernel();

console.log(`>>> VITALIS-PRIME Bridge active on port ${PORT}`);
console.log(`>>> Licensed to: ${AUTHOR}`);

module.exports = { pythonKernel, io };
