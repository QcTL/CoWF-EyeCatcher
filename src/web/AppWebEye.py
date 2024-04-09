import base64
from io import BytesIO

import matplotlib.pyplot as plt
from flask import Flask, render_template, Response
from flask_socketio import SocketIO

from src.runner.Eye.Eye import Eye
from src.runner.Eye.EyeContainer import EyeContainer


class AppWebEye:
    def __init__(self, eyeContainer: EyeContainer):
        self._eyeContainer: EyeContainer = eyeContainer
        self._app = Flask(__name__, template_folder='../../templates', static_folder='../../static')
        self._socketio = SocketIO(self._app)

        self._register_routes()

    def updateList(self, uuid, eye: Eye):
        print("UPDATED")
        print((uuid, eye))
        self._socketio.emit('list_updated', [uuid, eye.to_dict()])

    def updateGraf(self, uuid, eye: Eye):
        selEye = self._eyeContainer.getUniqueEye(uuid)
        img_base64 = self._getGraphGivenEye(selEye)
        self._socketio.emit('graph_updated', [uuid, img_base64])

    def _register_routes(self):
        @self._app.route('/')
        @self._app.route('/home')
        def endpointHome():
            return render_template('p_lEyes.html', lEyes=self._eyeContainer.getTotalEyes())

        @self._app.route('/eye/<eye_id>')
        def endpointEye(eye_id):
            selEye = self._eyeContainer.getUniqueEye(eye_id)
            # Encode the image as base64
            img_base64 = self._getGraphGivenEye(selEye)
            return render_template('p_graphEye.html', img_base64=img_base64,
                                   eye=selEye)

        @self._app.route('/download_csv/<eye_id>')
        def download_csv(eye_id):
            selEye = self._eyeContainer.getUniqueEye(eye_id)
            csv_data = "Index,Value\n"  # Header row
            for i, value in enumerate(selEye[1].eValues):
                csv_data += f"{i},{value}\n"
            return Response(
                csv_data,
                mimetype="text/csv",
                headers={"Content-disposition": f"attachment; filename={selEye[0]}.csv"}
            )

    def _getGraphGivenEye(self, selEye):
        fig, ax = plt.subplots(figsize=(12, 6), dpi=100)
        ax.plot(selEye[1].eTimes, selEye[1].eValues)
        ax.set_xlabel('Time', color='white')
        ax.set_ylabel(selEye[1].eName, color='white')
        ax.set_title('')

        ax.spines['bottom'].set_color('white')
        ax.spines['left'].set_color('white')

        ax.spines['top'].set_alpha(0)
        ax.spines['right'].set_alpha(0)

        ax.set_xticks([])
        ax.tick_params(axis='y', colors='white')
        fig.patch.set_alpha(0)
        ax.patch.set_alpha(0)

        img = BytesIO()
        plt.savefig(img, format='png', transparent=True)
        img.seek(0)

        return base64.b64encode(img.getvalue()).decode()

    def addNewInfo(self, llNewValues):
        for i in llNewValues:
            self._socketio.emit('list_updated', i)

    def start(self):
        self._socketio.run(self._app, allow_unsafe_werkzeug=True)
