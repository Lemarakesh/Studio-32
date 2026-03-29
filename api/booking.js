export default async function handler(req, res) {
    if (req.method === 'POST') {
        try {
            // We use a fixed subdomain for localtunnel so you don't have to keep updating it!
            const TUNNEL_URL = 'https://studio32.loca.lt/webhook/booking';
            
            const response = await fetch(TUNNEL_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Bypass-Tunnel-Reminder': 'true' // Vercel backend bypasses the warning screen!
                },
                body: JSON.stringify(req.body)
            });
            
            if (!response.ok) {
                throw new Error(`n8n responded with status: ${response.status}`);
            }

            res.status(200).json({ success: true, message: 'Sent successfully to n8n' });
        } catch (error) {
            console.error('Webhook Error:', error);
            res.status(500).json({ success: false, error: 'Could not reach n8n server' });
        }
    } else {
        res.status(405).json({ message: 'Only POST requests allowed' });
    }
}
