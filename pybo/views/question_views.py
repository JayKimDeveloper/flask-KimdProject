from datetime import datetime
from flask import Blueprint, render_template, request, url_for
from pybo.models import Question
from ..forms import QuestionForm, AnswerForm
from .. import db
from werkzeug.utils import redirect

bp = Blueprint('question', __name__, url_prefix='/question')

@bp.route('/list/')
def _list():
    page = request.args.get('page', type=int, default=1)  # 페이지
    question_list = Question.query.order_by(Question.create_date.desc())
    question_list = question_list.paginate(page, per_page=10)
    return render_template('question/question_list.html', question_list=question_list)

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    
    return render_template('question/question_detail.html', question=question, form=form)



@bp.route('/create/')
def create():
    form = QuestionForm()
    return render_template('question/question_form.html', form=form)