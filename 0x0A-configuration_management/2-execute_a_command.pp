# does stuff 

exec { 'pkill killmenow' :
    path    => '/bin/',
    command => 'pkill killmenow',
    }
