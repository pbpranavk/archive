import React from "react";

class Comments extends React.Component{

    constructor(props){
        super(props);
        self = this;
    }
    renderComment(comment, i){
        return(
            <div className="comment" key={i}>
                <p>
                    <strong>{comment.user}</strong>
                    {comment.text}
                    <button className="remove-comment" onClick={self.props.removeComment.bind(null, self.props.params.postId,i )}>&times;</button>
                </p>
            </div>
        );
    }
    handleSubmit(event){
        event.preventDefault();
        const {postId} = self.props.params;
        const author = self.refs.author.value;
        const comment = self.refs.comment.value;
        self.props.addComment(postId, author, comment);
        self.refs.commentForm.reset();
    }
    render(){
        return (
            <div className="comments">
                {self.props.postComments.map(this.renderComment)}
                <form ref="commentForm" className="comment-form" onSubmit={this.handleSubmit}>
                    <input type="text" ref="author" placeholder="author" />
                    <input type="text" ref="comment" placeholder="comment" />
                    <input type="submit" hidden />
                </form>
            </div>
        );
    }
}

export default Comments;