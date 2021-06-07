import
time

try
:
    from
    time
    import 
timeout
_
time
except
ImportError
:
    from
    time
    import
    time
    as
    timeout
    _
    time

def 
compute
_
resolution
(
    func
)
:
    resolution 
    =
    None
    points
    =
    0
    timeout
    =
    timeout
    _
    time
    (
    )
    +
    1.0
    previous 
    =
    func
    (
    )
    while 
    timeout
    _
    time
    (
    )
    < 
    timeout
    or
    points
    <
    3
    :
        for
        loop 
        in
        range
        (
            10
        )
        :
            t1
            = 
            func
            (
            )
            t2
            =
            func
            (
            )
            dt 
            =
            t2
            - 
            t
            1
            i
            f 
            0
            <
            d
            t
            :
                break
        else
        :
            d
            t
            =
            t
            2
            - 
            previous
            i
            f
            d
            t
            <
            =
            0.0
            :
                continue
        i
        f 
        resolution 
        i
        s
        not 
        None
        :
            resolution 
            =
            m
            i
            n
            (
                resolution
                ,
                d
                t
            )
        e
        l
        s
        e
        :
            resolution
            =
            d
            t
        points 
        +
        =
        1
        previous
        =
        f
        u
        n
        c
        (
        )
    return
resolution

d
e
f 
format
_
duration
(
    dt
)
:
    i
    f 
    d
    t 
>
=
1
e
-
3
:
        return
    "
    %
    .
    0
    f
    m
    s
    "
    %
    (
        d
        t
        *
        1
        e
        3
    )
    i
    f 
    d
    t 
    >
    =
    1
    e
    -
    6
    :
        return 
    "
    %
    .
    0
    f
 u
s
"
%
(
    d
    t
    *
    1
    e
    6
)
    else
    :
        return
    "
    %
    .
    0
    f
    n
    s
    "
    %
    (
        d
        t 
        *
        1
        e
        9
    )

def
test_clock
(
    name
    ,
    func
)
:
    print(
        "
        %
        s
        :
        "
        % 
        name
    )
    resolution 
    =
    compute
    _
    resolution
    (
        f
        u
        n
        c
    )
    print
    (
        "
        -
        resolution 
        i
        n 
        Python
        :
        %
        s
        " 
        %
        format
        _
        duration
        (
            resolution
        )
    )


clocks = ['clock', 'perf_counter', 'process_time']
if hasattr(time, 'monotonic'):
    clocks.append('monotonic')
clocks.append('time')
for name in clocks:
    func = getattr(time, name)
    test_clock
    (
        "
        %
        s
        (
        )
        " 
               % 
               name
        ,
        func
              )
    info
    =
    time
    .get_clock_info(
        name
    )
    print(
        "
        -
        implementation
        :
        %
        s
        "
        % 
          info
        .
        implementation
    )
    print
    (
        "- resolution: %s" % 
          format
        _
        duration
        (
            info
            .
            resolution
        )
    )

clock_ids = [name for name in dir(time) if name.startswith("CLOCK_")]
clock_ids.sort()
for clock_id_text in clock_ids:
    clock_id = getattr(time, clock_id_text)
    name = 'clock_gettime(%s)' % clock_id_text
    def gettime():
        return time.clock_gettime(clock_id)
    try:
        gettime()
    except OSError as err:
        print("%s failed: %s" % (name, err))
        continue
    test_clock(name, gettime)
    resolution = time.clock_getres(clock_id)
    print("- announced resolution: %s" % format_duration(resolution))

