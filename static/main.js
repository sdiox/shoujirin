/**
 * Created by sdiox on 7/1/15 AD.
 */
$(document).ready(function()
{
    var $btnSubmit = $('input#btnSubmit');
    var $txtKeyword = $('input#txtKeyword');
    var $chkLimit = $('input#chkFirstPage');
    var $btnLimit = $('span#btnLimit');
    var $hdnQueryLanguage = $('input#hdnQueryLanguage');

    var $navbar = $('.navbar');
    var $navbarTop = $('.navbar.navbar-fixed-top');
    var $navbarBottom = $('.navbar.navbar-fixed-bottom');
    var $lnkGoToTop = $navbarTop.find('a#lnkGoToTop');

    var areNavbarsTransparent = false;

    var txtKeywordBound = false;

    (function()
    {
        // normalize values in the checkbox
        // because of weird checkbox handling mechanism in WTF
        var chkLimitVal = $.trim($chkLimit.val()).toLowerCase();
        if(chkLimitVal == '' || chkLimitVal == 'true')
        {
            $chkLimit.prop('checked', true);
            $chkLimit.val('True');
        }
        else
        {
            $chkLimit.prop('checked', false);
            $chkLimit.val('False');
            $btnLimit.toggleClass('strikethrough alert-warning greyed-out');
        }

        // highlight the keyword
        var keyword = $txtKeyword.val();
        $('td:contains("' + keyword + '")').each(function(e)
        {
            var $elem = $(this);
            var _html = $elem.html();
            _html = _html.replace(keyword, '<span class="highlight">' + keyword + '</span>');
            $elem.html(_html);
        });

        wanakana.bind($txtKeyword.get(0));
        txtKeywordBound = !txtKeywordBound;
    })();

    $txtKeyword.keypress(function(e)
    {
       if(e.which == 13)
       {
           $txtKeyword.val($.trim($txtKeyword.val()));
           var keyword = $txtKeyword.val();

           var $divError = $('div.alert#divError');

           if(keyword.length < 1)
           {
               $divError.find('span#spanErrorMsg').text('empty input!');
               $divError.removeClass('hidden');

               return false;
           }
           else
           {
               $divError.addClass('hidden');
           }

           $btnSubmit.submit();
       }
       else
       {
           if(e.keyCode == 27 || e.which == 27)
           {
               $txtKeyword.val(wanakana.toRomaji($txtKeyword.val()));

               txtKeywordBound = !txtKeywordBound;
               if(txtKeywordBound)
               {
                   wanakana.bind($txtKeyword.get(0));
                   $txtKeyword.val(wanakana.toKana($txtKeyword.val()));
               }
               else
               {
                   wanakana.unbind($txtKeyword.get(0));
               }
           }
       }

    });

    $(document).click(function (event) 
    {
        event.stopPropagation();
        if($(event.target).is('html, body, div.container, div.row, p.muted-text, div.navbar-fixed-bottom, div.col-lg-12'))
            $txtKeyword.focus();
    });

    $txtKeyword.click(function() 
    {
        $txtKeyword.select();
    });

    $('span#btnLimit').click(function()
    {
        $chkLimit.prop('checked', !$chkLimit.prop('checked'));
        $chkLimit.val($chkLimit.prop('checked') ? 'True' : 'False');
        $btnLimit.toggleClass('strikethrough alert-warning greyed-out');
    });

    $('button#btnSearch').click(function(event)
    {
        event.preventDefault();

           $txtKeyword.val($.trim($txtKeyword.val()));
           var keyword = $txtKeyword.val();

           var $divError = $('div.alert#divError');

           if(keyword.length < 1)
           {
               $divError.find('span#spanErrorMsg').text('empty input!');
               $divError.removeClass('hidden');

               return false;
           }
           else
           {
               $divError.addClass('hidden');
           }

        $btnSubmit.trigger('click');
    });

    $(window).bind('scroll', function(event) 
    {
        var y_scroll_pos = window.pageYOffset;
        var y_pos_threshhold = 20;

        if(y_scroll_pos > y_pos_threshhold)
        {
            if(!areNavbarsTransparent)
            {
                areNavbarsTransparent = true;
                $navbarTop.fadeTo('400', 0.7);
                $navbarBottom.fadeTo('400', 0.0);

                $lnkGoToTop.fadeTo('400', 1.0);
            }
        }
        else 
        {
            if(areNavbarsTransparent)
            {
                areNavbarsTransparent = false;
                $navbar.fadeTo('400', 1.0);
                $lnkGoToTop.fadeTo('400', 0.0);
            }
        }
    });

    $lnkGoToTop.click(function(event)
    {
        event.preventDefault();
        $("html, body").animate({scrollTop: 0 },"fast");
        $lnkGoToTop.blur();
    });

    $(window).focus(function()
    {
        $txtKeyword.click();
    });
});