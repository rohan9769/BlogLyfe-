import React from 'react'
import Navbar from './Navbar'
import {Link , NavLink} from 'react-router-dom'

const Home = () => {
    return (
        <>
            <div className="container">
                <div className = "jumbotron mt-5">
                    <h1>Welcome to Blog Lyfe!</h1>
                    <p className="lead">We make all kinds of interesting blogs on various topics</p>
                    <hr className="my-4"></hr>
                    <p>Click the button below to checkout our Blogs</p>
                    <p className="lead">
                        <Link className="btn btn-primary btn-lg" to='/blog' role="button">Check out our blog</Link>
                    </p>
                </div>
            </div>
        </>
    )
}

export default Home
