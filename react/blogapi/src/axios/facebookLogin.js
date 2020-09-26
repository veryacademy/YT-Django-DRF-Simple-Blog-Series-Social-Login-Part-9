import axios from 'axios';
import { useHistory } from 'react-router-dom';

const facebookLogin = (accesstoken) => {
	console.log(accesstoken);
	axios
		.post('http://127.0.0.1:8000/auth/convert-token', {
			token: accesstoken,
			backend: 'facebook',
			grant_type: 'convert_token',
			client_id: '05GYopkyMDxFakgCSuNtpOLrNcyJwU054wZfYBt1',
			client_secret:
				'U3r3rmtff7t52Xa1chfzGf5vtl06zr4PwGbi8sWBcilTKs0YJEm278JPmXbcgMsyYpxYMQbDKFsyjhrzKwDLW8VMfW0ePZmrRuSmssnFPvqjeodYsNTfObTAzxOxZKuH',
		})
		.then((res) => {
			localStorage.setItem('access_token', res.data.access_token);
			localStorage.setItem('refresh_token', res.data.refresh_token);
		});
};

export default facebookLogin;
